
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4 (1.5 - 6.0s)

# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),   # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),   # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),    # G#
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),    # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),   # A#
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),   # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),    # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),    # D
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),   # D#
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),   # E
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),    # F
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # D
    # Bar 3: C7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif starts
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.6875, end=1.875), # B
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.1875, end=3.375), # B
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.6875, end=4.875), # B
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0625), # C
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.25), # B
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.4375), # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.4375, end=5.625), # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.625, end=5.8125), # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.8125, end=6.0),  # B
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start_time = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.375, end=start_time + 0.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.125, end=start_time + 1.3125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=start_time + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.3125, end=start_time + 1.5),
    drums.notes.extend([
        pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375),
        pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.75, end=start_time + 1.125),
        pretty_midi.Note(velocity=110, pitch=38, start=start_time + 0.375, end=start_time + 0.5625),
        pretty_midi.Note(velocity=110, pitch=38, start=start_time + 1.125, end=start_time + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time, end=start_time + 0.1875),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.1875, end=start_time + 0.375),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.375, end=start_time + 0.5625),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.5625, end=start_time + 0.75),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.75, end=start_time + 0.9375),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 0.9375, end=start_time + 1.125),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.125, end=start_time + 1.3125),
        pretty_midi.Note(velocity=90, pitch=42, start=start_time + 1.3125, end=start_time + 1.5),
    ])

midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI
midi.write('dante_intro.mid')
