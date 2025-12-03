
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane plays Dm7 -> G7 -> Cm7 -> F7 (open voicings)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),
]
piano.notes.extend(diane_notes)

# Marcus plays walking bass line (D2-G2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (beat 1)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25), # F2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # G2 (beat 3)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),  # E2 (beat 4)
]
bass.notes.extend(bass_notes)

# Dante plays sax melody: D -> F -> G -> D (staccato, legato on last note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4 (beat 1)
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # F4 (beat 2)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # G4 (beat 3)
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=3.0),  # D4 (beat 4, held)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane plays G7 -> Cm7 -> F7 -> Dm7 (open voicings)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=4.5),  # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),
]
piano.notes.extend(diane_notes)

# Marcus plays walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # G2 (beat 1)
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # E2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # D2 (beat 3)
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # F2 (beat 4)
]
bass.notes.extend(bass_notes)

# Dante plays sax melody: D -> Bb -> C -> D (staccato)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D4 (beat 1)
    pretty_midi.Note(velocity=110, pitch=57, start=3.125, end=3.25),  # Bb4 (beat 2)
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.375),  # C4 (beat 3)
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=4.5),   # D4 (beat 4, held)
]
sax.notes.extend(sax_notes)

# Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),   # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane plays F7 -> Dm7 -> G7 -> Cm7 (open voicings)
diane_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),
]
piano.notes.extend(diane_notes)

# Marcus plays walking bass line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=41, start=4.5, end=4.875),  # F2 (beat 1)
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # D2 (beat 2)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # G2 (beat 3)
    pretty_midi.Note(velocity=100, pitch=40, start=5.625, end=6.0),  # E2 (beat 4)
]
bass.notes.extend(bass_notes)

# Dante plays sax melody: D -> F -> G -> D (staccato)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D4 (beat 1)
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75),  # F4 (beat 2)
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),  # G4 (beat 3)
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=6.0),   # D4 (beat 4, held)
]
sax.notes.extend(sax_notes)

# Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),   # Hihat on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=38, start=5.625, end=6.0),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
