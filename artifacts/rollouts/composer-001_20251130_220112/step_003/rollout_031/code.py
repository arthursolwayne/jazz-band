
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for eighth in range(2):
        hihat_time = time + (eighth * bar_length / 8)
        note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start at 1.5 seconds

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.5 + 0.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=1.75 + 0.25), # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=2.0, end=2.0 + 0.25),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.25, end=2.25 + 0.25), # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.5 + 0.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=2.75 + 0.25), # B
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.0 + 0.25),  # C
    pretty_midi.Note(velocity=90, pitch=54, start=3.25, end=3.25 + 0.25), # C#
    pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=3.5 + 0.25),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=3.75 + 0.25), # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=4.0, end=4.0 + 0.25),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=4.25, end=4.25 + 0.25), # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.5 + 0.25),  # F#
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.75 + 0.25), # G
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=5.0 + 0.25),  # G#
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.25 + 0.25), # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 (F, A, C, Eb)
chord_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.75),  # Bb
]
piano.notes.extend(chord_notes)

# Bar 3: Bb7 (Bb, D, F, Ab)
chord_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),  # C
]
piano.notes.extend(chord_notes)

# Bar 4: E7 (E, G#, B, D)
chord_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # A#
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # C#
]
piano.notes.extend(chord_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, Ab, Bb, F (F7 arpeggio)
note1 = pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=110, pitch=55, start=1.75, end=2.0)
note3 = pretty_midi.Note(velocity=110, pitch=57, start=2.0, end=2.25)
note4 = pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.25)
sax.notes.extend([note1, note2, note3, note4])

# Drums: Continue in bars 2-4
for bar in range(2, 4):
    start_time = bar * bar_length
    for beat in range(4):
        time = start_time + (beat * bar_length / 4)
        if beat % 2 == 0:
            # Kick on 1 and 3
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        else:
            # Snare on 2 and 4
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Hihat on every eighth
        for eighth in range(2):
            hihat_time = time + (eighth * bar_length / 8)
            note = pretty_midi.Note(velocity=80, pitch=42, start=hihat_time, end=hihat_time + 0.05)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_intro.mid")
