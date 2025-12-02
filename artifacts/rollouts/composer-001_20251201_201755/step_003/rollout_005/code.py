
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # C2 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0)   # F2 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm9 (D, F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=3.0)   # E5
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif - start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D4 (root)
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # F4 (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # E4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0)   # Bb4 (suspension)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),  # F3 (root)
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # Eb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # D3 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5)   # Bb3 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 3: G7sus4 (G, C, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=4.5),  # C5
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5)   # F4
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif continuation, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # Bb4 (suspension)
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # F4 (resolve)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # E4 (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5)   # D4 (resolve)
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # D3 (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Bb3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # C3 (fifth)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0)   # F3 (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0)   # C4 (resolve)
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif continuation, finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D4 (resolve)
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0)   # D4
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125)
]
for note in drum_notes:
    drums.notes.append(note)

# Add hihat on every eighth for bars 2-4
for start in [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]:
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375)
    drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
