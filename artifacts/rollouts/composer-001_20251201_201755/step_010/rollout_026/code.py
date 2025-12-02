
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody starts
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # D (F7)
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # C (F7)
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0625), # D# (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=2.0625, end=2.25), # D (F7)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=1.6875, end=1.875), # G2
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.0625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=2.0625, end=2.25),  # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=2.25),  # F (F7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),  # A (F7)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),  # C (F7)
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # E (F7)
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.9375),  # D (Dm7)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.9375),  # F (Dm7)
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.9375),  # A (Dm7)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.9375),  # C (Dm7)
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.9375, end=3.625),  # G (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=2.9375, end=3.625),  # B (G7)
    pretty_midi.Note(velocity=90, pitch=64, start=2.9375, end=3.625),  # D (G7)
    pretty_midi.Note(velocity=90, pitch=57, start=2.9375, end=3.625),  # F (G7)
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1875),  # D (F7)
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # C (F7)
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.5625), # D# (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=3.5625, end=3.75), # D (F7)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.1875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=3.1875, end=3.375), # G2
    pretty_midi.Note(velocity=80, pitch=39, start=3.375, end=3.5625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=3.5625, end=3.75),  # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Drums: same pattern
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Complete motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6875),  # D (F7)
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # C (F7)
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.0625), # D# (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=5.0625, end=5.25), # D (F7)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (F2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.6875),  # F2
    pretty_midi.Note(velocity=80, pitch=40, start=4.6875, end=4.875), # G2
    pretty_midi.Note(velocity=80, pitch=39, start=4.875, end=5.0625), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=40, start=5.0625, end=5.25),  # G2
]
for note in bass_notes:
    bass.notes.append(note)

# Drums: same pattern
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Piano: Resolve on last chord
# Bar 4: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),  # G (G7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # B (G7)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.25),  # D (G7)
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=5.25),  # F (G7)
]
for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
