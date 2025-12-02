
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice. D minor
# Dm7 chord: D F A C
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0), # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5), # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875), # C
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0), # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7: D F A C
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875), # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875), # Bb
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375), # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375), # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875), # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875), # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875), # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 scale: D, Eb, F, G, A, Bb, C, D
# Motif: D, Eb, F, G (start), then leave it hanging on G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875), # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G (hold)
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.8125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.8125, end=3.0), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375), # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G (hold)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.9375, end=4.125), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.3125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.3125, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875), # G (hold)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0625), # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.0625, end=5.25), # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.4375), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625), # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    kick_start = start + 0.0
    kick_end = start + 0.375
    snare_start = start + 0.75
    snare_end = start + 0.875
    kick2_start = start + 1.125
    kick2_end = start + 1.5
    snare2_start = start + 1.875
    snare2_end = start + 2.0

    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_end),
    pretty_midi.Note(velocity=100, pitch=36, start=kick2_start, end=kick2_end),

    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=snare_start, end=snare_end),
    pretty_midi.Note(velocity=100, pitch=38, start=snare2_start, end=snare2_end),

    # Hihat
    for i in range(4):
        hihat_start = start + (i * 0.375)
        hihat_end = hihat_start + 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_russo_intro.mid')
