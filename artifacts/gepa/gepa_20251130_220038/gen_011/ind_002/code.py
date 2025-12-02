
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
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # C

    # Bar 3
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=95, pitch=72, start=3.0, end=3.375),  # C

    # Bar 4
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),  # C
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
