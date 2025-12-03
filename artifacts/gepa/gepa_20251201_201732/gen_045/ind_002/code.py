
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.6875),  # D2, root
    pretty_midi.Note(velocity=90, pitch=53, start=1.6875, end=1.875), # A2, fifth
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0625), # Eb2, chromatic approach
    pretty_midi.Note(velocity=90, pitch=50, start=2.0625, end=2.25), # D2, root
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.1875),  # D2, root
    pretty_midi.Note(velocity=90, pitch=53, start=3.1875, end=3.375), # A2, fifth
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.5625), # Bb2, chromatic approach
    pretty_midi.Note(velocity=90, pitch=50, start=3.5625, end=3.75), # D2, root
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.6875),  # D2, root
    pretty_midi.Note(velocity=90, pitch=53, start=4.6875, end=4.875), # A2, fifth
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.0625), # Eb2, chromatic approach
    pretty_midi.Note(velocity=90, pitch=50, start=5.0625, end=5.25), # D2, root
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6875), # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875), # A4
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875), # F4
]
# Bar 3: Bbmaj7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.1875), # Bb4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.1875), # E4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875), # A4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.1875), # C#5
])
# Bar 4: G7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6875), # G4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.6875), # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.6875), # D5
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6875), # A4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.4375), # F4
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875), # A4
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5625), # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.9375), # F4
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875), # G4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # A4
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.4375), # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875), # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
# Bar 3 (3.0 - 4.5s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
])
# Bar 4 (4.5 - 6.0s)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
