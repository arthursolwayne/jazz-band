
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Diane on 2 and 4, Marcus walking line, sax enters with motif

# Diane: 7th chords on 2 and 4
bar_start = 1.5
diane_notes = [
    # Bar 2: Fm7 on 2, Bbm7 on 4
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.75, end=bar_start + 1.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 0.75, end=bar_start + 1.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 0.75, end=bar_start + 1.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=76, start=bar_start + 0.75, end=bar_start + 1.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 1.5, end=bar_start + 1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=bar_start + 1.5, end=bar_start + 1.875),  # Db
    pretty_midi.Note(velocity=100, pitch=74, start=bar_start + 1.5, end=bar_start + 1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=79, start=bar_start + 1.5, end=bar_start + 1.875),  # G
]

# Marcus: Walking line, chromatic approaches, no repeated notes
# Fm: F, Gb, Ab, Bb, C, Db, Eb, F
# Walking line in Fm
marcus_notes = [
    # Bar 2: Walking line starting on F
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 0.0, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=65, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 1.125, end=bar_start + 1.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=72, start=bar_start + 1.5, end=bar_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=74, start=bar_start + 1.875, end=bar_start + 2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=bar_start + 2.25, end=bar_start + 2.625),
    pretty_midi.Note(velocity=100, pitch=79, start=bar_start + 2.625, end=bar_start + 3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=77, start=bar_start + 3.0, end=bar_start + 3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=bar_start + 3.375, end=bar_start + 3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=bar_start + 3.75, end=bar_start + 4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=bar_start + 4.125, end=bar_start + 4.5),
    # Bar 4 continuation
    pretty_midi.Note(velocity=100, pitch=67, start=bar_start + 4.5, end=bar_start + 4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=bar_start + 4.875, end=bar_start + 5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=bar_start + 5.25, end=bar_start + 5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=bar_start + 5.625, end=bar_start + 6.0),
]

# Dante: Motif in Fm, short, singable, leaves it hanging
# Motif: F (64), Ab (69), Bb (71), F (64)
# First bar of motif
dante_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 0.0, end=bar_start + 0.375),
    pretty_midi.Note(velocity=110, pitch=69, start=bar_start + 0.375, end=bar_start + 0.75),
    pretty_midi.Note(velocity=110, pitch=71, start=bar_start + 0.75, end=bar_start + 1.125),
    pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 1.125, end=bar_start + 1.5),
    # Repeat the motif in bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 3.0, end=bar_start + 3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=bar_start + 3.375, end=bar_start + 3.75),
    pretty_midi.Note(velocity=110, pitch=71, start=bar_start + 3.75, end=bar_start + 4.125),
    pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 4.125, end=bar_start + 4.5),
    # Final bar: End on F, leave it hanging
    pretty_midi.Note(velocity=110, pitch=64, start=bar_start + 4.5, end=bar_start + 6.0),
]

# Drums: Continue kicks on 1 and 3, snares on 2 and 4, hihat on every eighth
for bar in range(3):  # bars 2, 3, 4
    start = bar_start + bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Add notes to instruments
piano.notes.extend(diane_notes)
bass.notes.extend(marcus_notes)
sax.notes.extend(dante_notes)
drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
