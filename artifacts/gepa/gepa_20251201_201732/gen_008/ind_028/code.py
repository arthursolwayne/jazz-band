
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line: F2 (D), Ab2 (F), Bb2 (G), C2 (B)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F2 (D)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # Ab2 (F)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625), # Bb2 (G)
    pretty_midi.Note(velocity=90, pitch=40, start=2.625, end=3.0),  # C2 (B)
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, Eb) - open voicing, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25), # F4
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=2.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25), # C5
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.25), # Eb4
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0), # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=3.0), # F5
])
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (D), G (E), Ab (F), F (D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875), # F4
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.25), # G4
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.625), # Ab4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: Bb2 (F), C2 (F), D2 (G), Eb2 (B)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375), # Bb2 (F)
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # C2 (F)
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # D2 (G)
    pretty_midi.Note(velocity=90, pitch=39, start=4.125, end=4.5),  # Eb2 (B)
]
bass.notes.extend(bass_notes)

# Piano: Bb7 (Bb, D, F, Ab) - open voicing, resolve on the last
# Bar 3: Bb7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75), # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75), # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75), # F5
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.75), # Ab4
]
# Bar 4: C7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5), # C5
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5), # E5
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.5), # G5
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5), # B5
])
piano.notes.extend(piano_notes)

# Sax: Continue the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.375), # G4
    pretty_midi.Note(velocity=110, pitch=66, start=3.375, end=3.75), # G4 -> A4
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125), # A4
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),  # Resolve to F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: F2 (D), G2 (E), Ab2 (F), F2 (D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875), # F2 (D)
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # G2 (E)
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # Ab2 (F)
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),  # F2 (D)
]
bass.notes.extend(bass_notes)

# Piano: Fm7 (F, Ab, C, Eb) - final resolution
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25), # F4
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=5.25), # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25), # C5
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.25), # Eb4
]
piano.notes.extend(piano_notes)

# Sax: Final phrase, resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=5.25), # F4
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625), # G4
    pretty_midi.Note(velocity=110, pitch=61, start=5.625, end=6.0),  # Ab4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Hihat on 4
]
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
