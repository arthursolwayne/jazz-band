
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
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25), # E5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # E5
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875), # D3
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25), # Eb3
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.625), # E3
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0), # G3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25), # E
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25), # B
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0), # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0), # G
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0), # B
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Melody (repeat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # E5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5), # E5
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.375), # G3
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75), # Ab3
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125), # A3
    pretty_midi.Note(velocity=80, pitch=53, start=4.125, end=4.5), # Bb3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75), # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75), # B
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5), # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5), # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5), # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5), # B
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Melody (finish)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875), # D5
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # E5
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625), # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0), # E5
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line (chromatic)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875), # Bb3
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25), # B3
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625), # C4
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0), # Db4
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0), # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0), # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0), # B
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
