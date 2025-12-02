
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_3])

# Snare on 2 and 4
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_2, drum_snare_4])

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    note = pretty_midi.Note(velocity=90, pitch=42, start=start, end=end)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Marcus, walking line, chromatic approaches, no repeated notes
# C7 chord: C, E, B, Bb
# Walking line in C7
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=3.0),   # D#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
# C7: C E B Bb
# Comp on beat 2 and 4 of each bar
piano_notes = [
    # Bar 2 - beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),
    # Bar 2 - beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    # Bar 3 - beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    # Bar 3 - beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    # Bar 4 - beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    # Bar 4 - beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick_1, kick_3])

# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.25)
    drums.notes.extend([snare_2, snare_4])

# Hi-hat on every eighth
for start in range(3, 16):
    time = start * 0.375
    if time < 6.0:
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.375)
        drums.notes.append(note)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# C7: C E B Bb
# Motif: C (60) - E (64) - B (71) - Bb (67)
# Play first two notes (C, E), leave it hanging, then come back with B and Bb

# First two notes (C, E) at start of bar 2
sax_note_1 = pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875)
sax_note_2 = pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25)
sax.notes.extend([sax_note_1, sax_note_2])

# Rest of motif at start of bar 4
sax_note_3 = pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875)
sax_note_4 = pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25)
sax.notes.extend([sax_note_3, sax_note_4])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
