
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches
# Dm7 = D F A C
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.6875, end=1.875), # Eb (chromatic)
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0625), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.0625, end=2.25), # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.4375), # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.4375, end=2.625), # C
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=2.8125), # B (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=2.8125, end=3.0), # D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.5625), # C#
    pretty_midi.Note(velocity=80, pitch=62, start=3.5625, end=3.75), # D
    # Bar 4 continuation
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=3.9375), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.9375, end=4.125), # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.3125), # B (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=4.3125, end=4.5), # D
    # Bar 4 end
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.6875), # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.6875, end=4.875), # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.0625), # B (chromatic)
    pretty_midi.Note(velocity=80, pitch=62, start=5.0625, end=5.25), # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.4375), # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=61, start=5.625, end=5.8125), # C#
    pretty_midi.Note(velocity=80, pitch=62, start=5.8125, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Bar 2: comp on beat 2
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0), # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0), # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0), # C
    # Bar 3: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.8125, end=3.0), # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.8125, end=3.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.8125, end=3.0), # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.8125, end=3.0), # C
    # Bar 4: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.8125, end=4.0), # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.8125, end=4.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.8125, end=4.0), # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.8125, end=4.0), # C
    # Bar 4: comp on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=5.8125), # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.8125), # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=5.8125), # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4 (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.6875, end=1.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.4375, end=2.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.1875, end=3.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=3.9375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.9375, end=4.125), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.6875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.6875, end=4.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.4375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.4375, end=5.625), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

# Saxophone (Dante): motif in Dm, one short phrase, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0), # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.1875), # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=2.1875, end=2.375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5625), # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.5625, end=2.75), # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=2.9375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.9375, end=3.125), # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.3125), # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.3125, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.6875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.6875, end=3.875), # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.875, end=4.0), # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.1875), # E (tension)
    pretty_midi.Note(velocity=100, pitch=69, start=4.1875, end=4.375), # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.375, end=4.5), # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.6875), # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0), # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.1875), # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.1875, end=5.375), # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5625), # D (resolution)
    pretty_midi.Note(velocity=100, pitch=69, start=5.5625, end=5.75), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=5.9375), # F# (chromatic)
    pretty_midi.Note(velocity=100, pitch=69, start=5.9375, end=6.0), # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
