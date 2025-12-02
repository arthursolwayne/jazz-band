
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in F (F2, C3, G2, D3)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=78, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=80, pitch=84, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=80, pitch=77, start=2.25, end=2.625), # G2
    pretty_midi.Note(velocity=80, pitch=81, start=2.625, end=3.0),  # D3
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=95, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=87, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=91, start=1.5, end=1.875),  # E
]
for note in piano_notes_bar2:
    piano.notes.append(note)

# Bar 3: Bbmaj7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=95, pitch=75, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=80, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=87, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=88, start=2.25, end=2.625),  # Ab
]
for note in piano_notes_bar3:
    piano.notes.append(note)

# Bar 4: D7 (D, F#, A, C)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=95, pitch=80, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=85, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=87, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=84, start=2.625, end=3.0),  # C
]
for note in piano_notes_bar4:
    piano.notes.append(note)

# Dante: Sax melody in F
# Bar 2: Start the motif
sax_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=85, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=87, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=84, start=1.875, end=2.0),  # A
]
for note in sax_notes_bar2:
    sax.notes.append(note)

# Bar 3: Continue the motif
sax_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=85, start=2.375, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=2.5, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=87, start=2.625, end=2.75),  # B
]
for note in sax_notes_bar3:
    sax.notes.append(note)

# Bar 4: Resolve the motif
sax_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=84, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=82, start=2.875, end=3.0),  # G
]
for note in sax_notes_bar4:
    sax.notes.append(note)

# Bar 2-4: Drums continue
drum_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 4
]
for note in drum_notes_bar2:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
