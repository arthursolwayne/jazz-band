
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=51, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, Fm7, Bbm7, Fm7, Bbm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.125), # Gb
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=50, start=5.25, end=5.625), # Gb
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Dante: Tenor saxophone motif
# Fm7 -> Ab7 -> Bbmaj7 -> Fm7
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
