
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start of melody - a whisper
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=90, pitch=60, start=1.6875, end=1.875), # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),   # F5
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=1.5, end=1.6875),  # D3
    pretty_midi.Note(velocity=80, pitch=39, start=1.6875, end=1.875), # C3
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),   # Eb3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.6875),  # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=1.5, end=1.6875),  # F5
    pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.6875),  # A5
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.4375), # D4
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.4375), # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.4375), # F5
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.4375), # A5
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues, drums continue
# Sax: Continue the melody, let it breathe
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.1875),  # G5
    pretty_midi.Note(velocity=90, pitch=62, start=2.1875, end=2.375), # D4
    pretty_midi.Note(velocity=90, pitch=60, start=2.375, end=2.5625), # Bb4
    pretty_midi.Note(velocity=90, pitch=64, start=2.5625, end=2.75), # F5
]
sax.notes.extend(sax_notes)

# Bass: Walking line continuation
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.1875),  # G3
    pretty_midi.Note(velocity=80, pitch=40, start=2.1875, end=2.375), # D3
    pretty_midi.Note(velocity=80, pitch=39, start=2.375, end=2.5625), # C3
    pretty_midi.Note(velocity=80, pitch=41, start=2.5625, end=2.75),  # Eb3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.4375), # D4
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.4375), # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.4375), # F5
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.4375), # A5
    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=2.9375), # D4
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=2.9375), # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=2.75, end=2.9375), # F5
    pretty_midi.Note(velocity=85, pitch=74, start=2.75, end=2.9375), # A5
]
piano.notes.extend(piano_notes)

# Drums: Continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=2.875), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 6.0s)
# Sax: Finish the motif, make it cry
sax_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.1875),  # D4
    pretty_midi.Note(velocity=95, pitch=60, start=3.1875, end=3.375), # Bb4
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.5625), # F5
    pretty_midi.Note(velocity=95, pitch=62, start=3.5625, end=3.75),  # D4
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=3.9375),  # Bb4
    pretty_midi.Note(velocity=95, pitch=64, start=3.9375, end=4.125), # F5
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.3125), # D4
    pretty_midi.Note(velocity=95, pitch=60, start=4.3125, end=4.5),   # Bb4
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.6875),   # F5
    pretty_midi.Note(velocity=95, pitch=62, start=4.6875, end=4.875), # D4
    pretty_midi.Note(velocity=95, pitch=60, start=4.875, end=5.0625), # Bb4
    pretty_midi.Note(velocity=95, pitch=64, start=5.0625, end=5.25), # F5
    pretty_midi.Note(velocity=95, pitch=62, start=5.25, end=5.4375), # D4
    pretty_midi.Note(velocity=95, pitch=60, start=5.4375, end=5.625), # Bb4
    pretty_midi.Note(velocity=95, pitch=64, start=5.625, end=5.8125), # F5
    pretty_midi.Note(velocity=95, pitch=62, start=5.8125, end=6.0)    # D4
]
sax.notes.extend(sax_notes)

# Bass: Walking line continuation
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.1875),  # Eb3
    pretty_midi.Note(velocity=80, pitch=43, start=3.1875, end=3.375), # G3
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.5625), # D3
    pretty_midi.Note(velocity=80, pitch=39, start=3.5625, end=3.75),  # C3
    pretty_midi.Note(velocity=80, pitch=41, start=3.75, end=3.9375),  # Eb3
    pretty_midi.Note(velocity=80, pitch=43, start=3.9375, end=4.125), # G3
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.3125), # D3
    pretty_midi.Note(velocity=80, pitch=39, start=4.3125, end=4.5),   # C3
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.6875),   # Eb3
    pretty_midi.Note(velocity=80, pitch=43, start=4.6875, end=4.875), # G3
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.0625), # D3
    pretty_midi.Note(velocity=80, pitch=39, start=5.0625, end=5.25),  # C3
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.4375),  # Eb3
    pretty_midi.Note(velocity=80, pitch=43, start=5.4375, end=5.625), # G3
    pretty_midi.Note(velocity=80, pitch=40, start=5.625, end=5.8125), # D3
    pretty_midi.Note(velocity=80, pitch=39, start=5.8125, end=6.0),   # C3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, with some tension
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.1875),  # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.1875),  # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=3.0, end=3.1875),  # F5
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.1875),  # A5
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=3.9375), # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=3.9375), # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=3.9375), # F5
    pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=3.9375), # A5
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.6875),   # D4
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.6875),   # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=4.5, end=4.6875),   # F5
    pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.6875),   # A5
    pretty_midi.Note(velocity=85, pitch=62, start=5.25, end=5.4375), # D4
    pretty_midi.Note(velocity=85, pitch=67, start=5.25, end=5.4375), # Bb4
    pretty_midi.Note(velocity=85, pitch=71, start=5.25, end=5.4375), # F5
    pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.4375), # A5
]
piano.notes.extend(piano_notes)

# Drums: Continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to a file
midi.save('dante_intro.mid')
