
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3 (beat 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4 (beat 1 and 3)
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # F#
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75), # D#
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125), # D#
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25), # A#
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625), # A#
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F7 - C
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # F7 - D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F7 - C
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # F7 - D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F7 - F
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # F7 - A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F7 - C
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # F7 - D
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3 (beat 0 and 2)
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4 (beat 1 and 3)
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Bb - D - A (F7 arpeggio)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.0625, end=2.25), # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.5625, end=3.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.25), # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.4375),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.4375, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.8125), # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.8125, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro_wayne.mid")
