
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.375, end=time + eighth * 0.375 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - Fm7, Bb7, Eb7, Ab7
bass_notes = [
    # Bar 2: Fm7 - root (F) and fifth (C), with chromatic approach
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.5 + 0.1),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 0.25, end=1.5 + 0.35),  # Bb
    pretty_midi.Note(velocity=80, pitch=41, start=1.5 + 0.5, end=1.5 + 0.6),  # C
    pretty_midi.Note(velocity=80, pitch=40, start=1.5 + 0.75, end=1.5 + 0.85),  # Bb

    # Bar 3: Bb7 - root (Bb) and fifth (F), with chromatic approach
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.0 + 0.1),  # Bb
    pretty_midi.Note(velocity=80, pitch=41, start=3.0 + 0.25, end=3.0 + 0.35),  # C
    pretty_midi.Note(velocity=80, pitch=42, start=3.0 + 0.5, end=3.0 + 0.6),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=3.0 + 0.75, end=3.0 + 0.85),  # C

    # Bar 4: Eb7 - root (Eb) and fifth (Bb), with chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.5 + 0.1),  # Eb
    pretty_midi.Note(velocity=80, pitch=44, start=4.5 + 0.25, end=4.5 + 0.35),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=4.5 + 0.5, end=4.5 + 0.6),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=4.5 + 0.75, end=4.5 + 0.85),  # F
]
bass.notes.extend(bass_notes)

# Piano (Diane) - Open voicings, different chord each bar, resolve on the last
def add_piano_notes(start_time, chord):
    # Root and 7th
    root = chord[0]
    seventh = chord[1]
    # Add root, major third, fifth, and seventh
    for pitch in chord:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start_time, end=start_time + 0.5)
        piano.notes.append(note)

# Bar 2: Fm7 (F, Ab, C, Db)
add_piano_notes(1.5, [39, 41, 43, 42])

# Bar 3: Bb7 (Bb, D, F, Ab)
add_piano_notes(3.0, [40, 44, 43, 41])

# Bar 4: Eb7 (Eb, G, Bb, Db)
add_piano_notes(4.5, [43, 47, 40, 42])

# Saxophone (Dante) - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Bb, C, G (Fm scale, but with a twist)
# Bar 2: Start the motif
note1 = pretty_midi.Note(velocity=110, pitch=39, start=1.5, end=1.5 + 0.25)
note2 = pretty_midi.Note(velocity=110, pitch=40, start=1.5 + 0.5, end=1.5 + 0.75)
note3 = pretty_midi.Note(velocity=110, pitch=41, start=1.5 + 1.0, end=1.5 + 1.25)
note4 = pretty_midi.Note(velocity=110, pitch=45, start=1.5 + 1.5, end=1.5 + 1.75)
sax.notes.extend([note1, note2, note3, note4])

# Bar 3: Repeat the motif
note5 = pretty_midi.Note(velocity=110, pitch=39, start=3.0, end=3.0 + 0.25)
note6 = pretty_midi.Note(velocity=110, pitch=40, start=3.0 + 0.5, end=3.0 + 0.75)
note7 = pretty_midi.Note(velocity=110, pitch=41, start=3.0 + 1.0, end=3.0 + 1.25)
note8 = pretty_midi.Note(velocity=110, pitch=45, start=3.0 + 1.5, end=3.0 + 1.75)
sax.notes.extend([note5, note6, note7, note8])

# Bar 4: Finish the motif
note9 = pretty_midi.Note(velocity=110, pitch=39, start=4.5, end=4.5 + 0.25)
note10 = pretty_midi.Note(velocity=110, pitch=40, start=4.5 + 0.5, end=4.5 + 0.75)
note11 = pretty_midi.Note(velocity=110, pitch=41, start=4.5 + 1.0, end=4.5 + 1.25)
note12 = pretty_midi.Note(velocity=110, pitch=45, start=4.5 + 1.5, end=4.5 + 1.75)
sax.notes.extend([note9, note10, note11, note12])

# Drums for bars 2-4
for bar in range(2, 4):
    start = bar * bar_length
    for beat in range(4):
        time = start + beat * bar_length / 4
        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hihat on every eighth
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.375, end=time + eighth * 0.375 + 0.05)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
