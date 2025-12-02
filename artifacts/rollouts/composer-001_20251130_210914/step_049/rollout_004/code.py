
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

# Bass line - walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=54, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=57, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=56, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.25), # B
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # D
    # Bar 3 - F7 on beat 4
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # D
    # Bar 4 - F7 on beat 2 and 4
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Start the motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # Bb
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),   # C
    # Bar 4 - Come back and finish it
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),   # C
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=5.75, end=6.0),   # C
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
]
# Bar 3
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5625))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5625, end=4.75))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.9375))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.9375, end=5.125))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.3125))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.3125, end=5.5))
# Bar 4
drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drum_notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375))
drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
