
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
# Bass: D2 (D) - G2 (G) - F2 (F) - C2 (C) - walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875), # D2 on 1
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # G2 on 2
    pretty_midi.Note(velocity=90, pitch=41, start=2.25, end=2.625), # F2 on 3
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0), # C2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875), # G4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875), # F4
]
# Bar 3: F7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # C5
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625), # E5
])
# Bar 4: Gm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0), # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25), # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.875), # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375), # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: C2 (C) - E2 (E) - F2 (F) - A2 (A)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375), # C2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75), # E2 on 2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # F2 on 3
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5), # A2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: F7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375), # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # C5
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375), # E5
]
# Bar 4: Gm7
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # Bb4
])
# Bar 4: Gm7 (resolve)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.5), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.5), # Bb4
])
piano.notes.extend(piano_notes)

# Drums: Bar 3
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
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Bb2 (Bb) - D2 (D) - E2 (E) - G2 (G)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875), # Bb2 on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25), # D2 on 2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # E2 on 3
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0), # G2 on 4
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Gm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875), # D5
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # Bb4
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
