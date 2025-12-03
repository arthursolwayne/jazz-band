
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
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=85, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (D2, F#2, chromatic approach to G2)
    pretty_midi.Note(velocity=70, pitch=38, start=1.5, end=1.5 + 0.375),  # D2
    pretty_midi.Note(velocity=70, pitch=40, start=1.875, end=1.875 + 0.375),  # F#2
    pretty_midi.Note(velocity=70, pitch=41, start=2.25, end=2.25 + 0.375),  # chromatic approach to G2
    pretty_midi.Note(velocity=70, pitch=43, start=2.625, end=2.625 + 0.375),  # G2

    # Bar 3 (A2, C#2, chromatic approach to D2)
    pretty_midi.Note(velocity=70, pitch=45, start=2.625, end=2.625 + 0.375),  # A2
    pretty_midi.Note(velocity=70, pitch=47, start=3.0, end=3.0 + 0.375),  # C#2
    pretty_midi.Note(velocity=70, pitch=46, start=3.375, end=3.375 + 0.375),  # chromatic approach to D2
    pretty_midi.Note(velocity=70, pitch=38, start=3.75, end=3.75 + 0.375),  # D2

    # Bar 4 (F#2, A2, chromatic approach to Bb2)
    pretty_midi.Note(velocity=70, pitch=40, start=3.75, end=3.75 + 0.375),  # F#2
    pretty_midi.Note(velocity=70, pitch=45, start=4.125, end=4.125 + 0.375),  # A2
    pretty_midi.Note(velocity=70, pitch=46, start=4.5, end=4.5 + 0.375),  # chromatic approach to Bb2
    pretty_midi.Note(velocity=70, pitch=44, start=4.875, end=4.875 + 0.375),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.5 + 0.125),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.5 + 0.125),  # F#4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.5 + 0.125),  # A4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.5 + 0.125),  # C#5
]

# Bar 3: G7 (G, B, D, F#)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.625 + 0.125),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.625 + 0.125),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.625 + 0.125),  # D4
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.625 + 0.125),  # F#5
])

# Bar 4: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.75 + 0.125),  # Bb4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.75 + 0.125),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.75 + 0.125),  # F4
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=3.75 + 0.125),  # Ab4
])
piano.notes.extend(piano_notes)

# Drums: continue with kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=90, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=85, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F#4, A4, D5 (half note, half note, quarter note, quarter note)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4 (half note)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # F#4 (half note)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A4 (quarter note)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D5 (quarter note)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
