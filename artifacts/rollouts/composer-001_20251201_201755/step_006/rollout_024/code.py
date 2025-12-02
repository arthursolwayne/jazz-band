
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

# Drums in Bar 1
bar1_start = 0.0
bar1_end = 1.5
kick_notes = [36]
snare_notes = [38]
hihat_notes = [42]

# Kick on 1 and 3
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
for time in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [bar1_start + i * 0.375 for i in range(4)]
for time in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus (bass): Walking line in Fm, roots and fifths with chromatic approaches
bar2_start = 1.5
bar2_end = 3.0
bass_notes = [
    # Fm root (F) with chromatic approach from E
    pretty_midi.Note(velocity=100, pitch=53, start=bar2_start + 0.0, end=bar2_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=51, start=bar2_start + 0.375, end=bar2_start + 0.75),
    # Bb (fifth of Fm) with chromatic approach from A#
    pretty_midi.Note(velocity=100, pitch=61, start=bar2_start + 0.75, end=bar2_start + 1.125),
    pretty_midi.Note(velocity=100, pitch=60, start=bar2_start + 1.125, end=bar2_start + 1.5),
    # Ab (bass note on beat 3)
    pretty_midi.Note(velocity=100, pitch=58, start=bar2_start + 1.5, end=bar2_start + 1.875),
    pretty_midi.Note(velocity=100, pitch=59, start=bar2_start + 1.875, end=bar2_start + 2.25),
    # Eb (bass note on beat 4)
    pretty_midi.Note(velocity=100, pitch=55, start=bar2_start + 2.25, end=bar2_start + 2.625),
    pretty_midi.Note(velocity=100, pitch=56, start=bar2_start + 2.625, end=bar2_start + 3.0)
]
for note in bass_notes:
    bass.notes.append(note)

# Diane (piano): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, Bb, D)
# Open voicing: F (53), Ab (58), Bb (61), D (62)
note1 = pretty_midi.Note(velocity=100, pitch=53, start=bar2_start, end=bar2_start + 0.75)
note2 = pretty_midi.Note(velocity=100, pitch=58, start=bar2_start, end=bar2_start + 0.75)
note3 = pretty_midi.Note(velocity=100, pitch=61, start=bar2_start, end=bar2_start + 0.75)
note4 = pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + 0.75)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 3: Bb7 (Bb, D, F, Ab)
# Open voicing: Bb (61), D (62), F (53), Ab (58)
note1 = pretty_midi.Note(velocity=100, pitch=61, start=bar2_start + 1.5, end=bar2_start + 2.25)
note2 = pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + 1.5, end=bar2_start + 2.25)
note3 = pretty_midi.Note(velocity=100, pitch=53, start=bar2_start + 1.5, end=bar2_start + 2.25)
note4 = pretty_midi.Note(velocity=100, pitch=58, start=bar2_start + 1.5, end=bar2_start + 2.25)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Bar 4: Eb7 (Eb, G, Bb, Db)
# Open voicing: Eb (55), G (57), Bb (61), Db (59)
note1 = pretty_midi.Note(velocity=100, pitch=55, start=bar2_start + 3.0, end=bar2_start + 3.75)
note2 = pretty_midi.Note(velocity=100, pitch=57, start=bar2_start + 3.0, end=bar2_start + 3.75)
note3 = pretty_midi.Note(velocity=100, pitch=61, start=bar2_start + 3.0, end=bar2_start + 3.75)
note4 = pretty_midi.Note(velocity=100, pitch=59, start=bar2_start + 3.0, end=bar2_start + 3.75)
piano.notes.append(note1)
piano.notes.append(note2)
piano.notes.append(note3)
piano.notes.append(note4)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (66), C (67), Gb (65), F (66)
# Start on beat 2 of bar 2, leave it hanging until beat 3 of bar 3
# Then come back and finish it in bar 4

# First phrase: F (66), C (67), Gb (65)
note1 = pretty_midi.Note(velocity=100, pitch=66, start=bar2_start + 0.75, end=bar2_start + 1.125)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=bar2_start + 1.125, end=bar2_start + 1.5)
note3 = pretty_midi.Note(velocity=100, pitch=65, start=bar2_start + 1.5, end=bar2_start + 1.875)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)

# Second phrase: F (66)
note1 = pretty_midi.Note(velocity=100, pitch=66, start=bar2_start + 3.0, end=bar2_start + 3.375)
sax.notes.append(note1)

# Drums in Bars 2-4
bar2_3_4_start = 1.5
bar2_3_4_end = 6.0

# Kick on 1 and 3 for each bar
kick_times = [
    bar2_3_4_start + 0.375,
    bar2_3_4_start + 1.125,
    bar2_3_4_start + 1.875,
    bar2_3_4_start + 2.625,
    bar2_3_4_start + 3.375,
    bar2_3_4_start + 4.125,
    bar2_3_4_start + 4.875,
    bar2_3_4_start + 5.625
]
for time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4 for each bar
snare_times = [
    bar2_3_4_start + 0.75,
    bar2_3_4_start + 1.5,
    bar2_3_4_start + 2.25,
    bar2_3_4_start + 3.0,
    bar2_3_4_start + 3.75,
    bar2_3_4_start + 4.5,
    bar2_3_4_start + 5.25,
    bar2_3_4_start + 6.0
]
for time in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [bar2_3_4_start + i * 0.375 for i in range(12)]
for time in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
