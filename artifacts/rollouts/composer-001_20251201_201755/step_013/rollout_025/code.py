
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
    # Hi-hat on every eighth
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

# Bass: walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (40) -> Bb (46) with chromatic approach from E (44)
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=44, start=1.625, end=1.75),
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=2.0),
    # Bar 3: Ab (43) -> D (47) with chromatic approach from C (40)
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=40, start=2.125, end=2.25),
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.5),
    # Bar 4: Bb (46) -> F (40) with chromatic approach from A (45)
    pretty_midi.Note(velocity=90, pitch=46, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=40, start=2.75, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F A C Eb) - open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # Eb
    # Bar 3: Ab7 (Ab C Eb G) - open voicing
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # G
    # Bar 4: Fm7 (F A C Eb) - open voicing, resolving on the last note
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (64) -> G (66) -> F (64) -> Eb (67) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=110, pitch=64, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=110, pitch=66, start=2.875, end=3.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0),
]
drums.notes.extend(drum_notes)

# Drums: Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.8125, end=4.0),
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
