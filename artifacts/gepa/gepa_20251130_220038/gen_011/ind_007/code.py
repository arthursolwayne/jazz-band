
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),  # F#
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.625),  # Ab
    # Fill on beat 3
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.0),  # Db
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125),  # Ab
    # Fill on beat 3
    pretty_midi.Note(velocity=90, pitch=67, start=2.375, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.5),  # Db
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.625),  # Ab
    # Fill on beat 3
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),  # Db
]
piano.notes.extend(piano_notes)

# Sax (Dante): Motif in Fm
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # F#
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=66, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.0),  # F#
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.625, end=1.75),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),  # Snare
]
# Hihat on every eighth
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.125),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=2.75, end=2.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.125, end=2.25),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),  # Snare
]
# Hihat on every eighth
for i in range(4):
    start = 2.0 + i * 0.375
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.25),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),  # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),  # Snare
]
# Hihat on every eighth
for i in range(4):
    start = 2.5 + i * 0.375
    end = start + 0.1875
    drum_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
