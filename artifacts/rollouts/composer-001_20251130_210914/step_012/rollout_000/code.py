
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

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875),  # Fm root
    pretty_midi.Note(velocity=90, pitch=50, start=1.6875, end=1.875), # Fm b9
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.0625), # Fm 9
    pretty_midi.Note(velocity=90, pitch=53, start=2.0625, end=2.25), # Fm 11
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.4375), # Fm 13
    pretty_midi.Note(velocity=90, pitch=53, start=2.4375, end=2.625), # Fm 11
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=2.8125), # Fm 9
    pretty_midi.Note(velocity=90, pitch=50, start=2.8125, end=3.0), # Fm b9
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.1875), # Fm root
    pretty_midi.Note(velocity=90, pitch=50, start=3.1875, end=3.375), # Fm b9
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.5625), # Fm 9
    pretty_midi.Note(velocity=90, pitch=53, start=3.5625, end=3.75), # Fm 11
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=3.9375), # Fm 13
    pretty_midi.Note(velocity=90, pitch=53, start=3.9375, end=4.125), # Fm 11
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.3125), # Fm 9
    pretty_midi.Note(velocity=90, pitch=50, start=4.3125, end=4.5), # Fm b9
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.6875), # Fm root
    pretty_midi.Note(velocity=90, pitch=50, start=4.6875, end=4.875), # Fm b9
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.0625), # Fm 9
    pretty_midi.Note(velocity=90, pitch=53, start=5.0625, end=5.25), # Fm 11
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.4375), # Fm 13
    pretty_midi.Note(velocity=90, pitch=53, start=5.4375, end=5.625), # Fm 11
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=5.8125), # Fm 9
    pretty_midi.Note(velocity=90, pitch=50, start=5.8125, end=6.0), # Fm b9
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.6875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.6875), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.6875), # G
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.6875), # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375), # C
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.4375), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.4375), # G
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.4375), # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875), # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875), # Eb
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.1875), # G
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.1875), # Bb
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.6875), # Gm (Fm ii)
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875), # F
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0625), # Gm
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375), # D (Gm7)
    pretty_midi.Note(velocity=110, pitch=64, start=2.4375, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.8125), # Gm
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.1875), # C (Fm7)
    pretty_midi.Note(velocity=110, pitch=71, start=3.1875, end=3.375), # Eb
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=110, pitch=66, start=3.5625, end=3.75), # Gm
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.9375), # F
    pretty_midi.Note(velocity=110, pitch=66, start=3.9375, end=4.125), # Gm
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.3125), # C
    pretty_midi.Note(velocity=110, pitch=71, start=4.3125, end=4.5), # Eb
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.6875), # C
    pretty_midi.Note(velocity=110, pitch=66, start=4.6875, end=4.875), # Gm
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.0625, end=5.25), # Gm
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.4375), # C
    pretty_midi.Note(velocity=110, pitch=71, start=5.4375, end=5.625), # Eb
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=5.8125), # C
    pretty_midi.Note(velocity=110, pitch=66, start=5.8125, end=6.0), # Gm
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
