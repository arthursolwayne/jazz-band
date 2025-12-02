
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
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F (F2, A2, C3, D3, F3, G3, A3, C4)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=82, start=1.875, end=2.25), # A2
    pretty_midi.Note(velocity=90, pitch=84, start=2.25, end=2.625), # C3
    pretty_midi.Note(velocity=90, pitch=85, start=2.625, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, chord on bar 2 and 4
# Bar 2: F7 (F, A, C, E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=3.0),  # E
]
# Bar 4: Gm7 (G, Bb, D, F)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # F
]
piano.notes.extend(piano_notes_bar2)
piano.notes.extend(piano_notes_bar4)

# Sax: One short motif in F, starting with a chromatic approach to F
# F (77), Eb (76), F (77), G (78) — then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=76, start=1.5, end=1.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=77, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=2.25, end=2.625),  # G
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2, A2, C3, D3, F3, G3, A3, C4)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=82, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=84, start=3.75, end=4.125), # C3
    pretty_midi.Note(velocity=90, pitch=85, start=4.125, end=4.5),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, chord on bar 2 and 4
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=4.5),  # Ab
]
piano.notes.extend(piano_notes_bar3)

# Drums: Same pattern as bar 1
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2, A2, C3, D3, F3, G3, A3, C4)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=82, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=84, start=5.25, end=5.625), # C3
    pretty_midi.Note(velocity=90, pitch=85, start=5.625, end=6.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, F)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # F
]
piano.notes.extend(piano_notes_bar4)

# Sax: Return to motif, finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=77, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums: Same pattern as bar 1
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
