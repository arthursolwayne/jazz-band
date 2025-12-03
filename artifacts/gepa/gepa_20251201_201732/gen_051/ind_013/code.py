
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
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5), # Snare on 4
    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start on beat 1
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5), # C4
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=2.75), # B3
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in Fm, starting on F2 (MIDI 38)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=37, start=2.25, end=2.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0), # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, unresolved, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 - open voicing
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.0), # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0), # C5
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0), # D4
    # Bar 3: Bbm7 - open voicing
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.75), # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.75), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.75), # F4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.75), # A4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of motif, incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0), # C4
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25), # B3
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=90, pitch=37, start=3.75, end=4.125), # E2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5), # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, unresolved
piano_notes = [
    # Bar 3: Fm7 - open voicing
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.5), # A4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5), # C5
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5), # D4
    # Bar 4: Bbm7 - open voicing
    pretty_midi.Note(velocity=90, pitch=61, start=3.75, end=4.25), # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.25), # D4
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.25), # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.25), # A4
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolution on beat 4
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75), # C4
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0), # D4
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5), # C4
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0), # F4 (resolution)
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875), # F2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=90, pitch=37, start=5.25, end=5.625), # E2
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0), # F2
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 4: Fm7 - open voicing
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0), # F4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.0), # A4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0), # C5
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0), # D4
    # Bar 4: Cm7 - open voicing (resolve on Cm)
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=6.0), # C4
    pretty_midi.Note(velocity=90, pitch=63, start=5.0, end=6.0), # E4
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=6.0), # G4
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=6.0), # A4
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0), # Snare on 4
    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
