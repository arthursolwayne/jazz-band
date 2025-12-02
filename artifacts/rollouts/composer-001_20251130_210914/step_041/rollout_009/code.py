
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

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0625), # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.0625, end=2.25), # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.4375), # A
    pretty_midi.Note(velocity=90, pitch=53, start=2.4375, end=2.625), # A#
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=2.8125), # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.8125, end=3.0), # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=3.0, end=3.1875), # B
    pretty_midi.Note(velocity=90, pitch=55, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.5625, end=3.75), # A#
    # Bar 4 (end)
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=3.9375), # A
    pretty_midi.Note(velocity=90, pitch=51, start=3.9375, end=4.125), # G#
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.3125), # G
    pretty_midi.Note(velocity=90, pitch=49, start=4.3125, end=4.5), # F#
    # Bar 4 (final)
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.6875), # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.6875, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.0625), # Eb
    pretty_midi.Note(velocity=90, pitch=45, start=5.0625, end=5.25), # D
    # Bar 4 (end)
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.4375), # Db
    pretty_midi.Note(velocity=90, pitch=43, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125), # Bb
    pretty_midi.Note(velocity=90, pitch=41, start=5.8125, end=6.0), # B
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2)
    pretty_midi.Note(velocity=95, pitch=59, start=1.875, end=2.0), # F7: F, A, C, Eb
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=85, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.0),
    # Bar 3 (comp on 2)
    pretty_midi.Note(velocity=95, pitch=59, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=85, pitch=64, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=60, start=2.8125, end=3.0),
    # Bar 4 (comp on 2)
    pretty_midi.Note(velocity=95, pitch=59, start=3.8125, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.8125, end=4.0),
    pretty_midi.Note(velocity=85, pitch=64, start=3.8125, end=4.0),
    pretty_midi.Note(velocity=80, pitch=60, start=3.8125, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax (Dante): Melody - one short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0), # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.4375), # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.4375, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.8125), # E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375), # F (elongated)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75), # G (elongated)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # E (elongated)
    # Bar 4 (finish)
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5), # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25), # E
    # Bar 4 (ending)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0), # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = 1.5 * bar
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat
    for eighth in range(8):
        start = bar_start + (eighth * 0.1875)
        end = start + 0.1875
        pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
    drums.notes.extend([pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
                        pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
                        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
                        pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)])
    for eighth in range(8):
        start = bar_start + (eighth * 0.1875)
        end = start + 0.1875
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
