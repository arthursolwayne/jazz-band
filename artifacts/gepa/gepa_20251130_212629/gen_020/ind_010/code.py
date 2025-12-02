
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
drum_notes = [
    (36, 0.0),  # Kick on 1
    (38, 0.375),  # Snare on 2
    (36, 0.75),  # Kick on 3
    (38, 1.125),  # Snare on 4
    (42, 0.0),  # Hihat on 1
    (42, 0.1875),  # Hihat on 1+
    (42, 0.375),  # Hihat on 2
    (42, 0.5625),  # Hihat on 2+
    (42, 0.75),  # Hihat on 3
    (42, 0.9375),  # Hihat on 3+
    (42, 1.125),  # Hihat on 4
    (42, 1.3125)  # Hihat on 4+
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax - Melody: Fm (F, Ab, Bb, Dm)
# Start with a motif: F (beat 1), Bb (beat 2), rest on beat 3, Ab on beat 4
sax_notes = [
    (84, 1.5),  # F
    (81, 1.875),  # Bb
    (84, 2.25),  # F (rest on beat 3)
    (81, 2.625),  # Ab
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bass - Walking line in Fm
# F, Gb, Ab, A, Bb, B, C, Db
bass_notes = [
    (53, 1.5),  # F
    (52, 1.875),  # Gb
    (51, 2.25),  # Ab
    (52, 2.625),  # A
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano - 7th chords on 2 and 4
# F7 on beat 2 (F, A, C, Eb)
# Bb7 on beat 4 (Bb, D, F, Ab)
piano_notes = [
    (53, 1.875),  # F
    (58, 1.875),  # A
    (57, 1.875),  # C
    (55, 1.875),  # Eb
    (58, 2.625),  # Bb
    (62, 2.625),  # D
    (57, 2.625),  # F
    (51, 2.625),  # Ab
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Drums - Bar 2
drum_notes = [
    (36, 1.5),  # Kick on 1
    (38, 1.875),  # Snare on 2
    (36, 2.25),  # Kick on 3
    (38, 2.625),  # Snare on 4
    (42, 1.5),  # Hihat on 1
    (42, 1.6875),  # Hihat on 1+
    (42, 1.875),  # Hihat on 2
    (42, 2.0625),  # Hihat on 2+
    (42, 2.25),  # Hihat on 3
    (42, 2.4375),  # Hihat on 3+
    (42, 2.625),  # Hihat on 4
    (42, 2.8125)  # Hihat on 4+
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - Melody: Repeat the motif, but shift it up a half step (G, C, rest on beat 3, Bb on beat 4)
sax_notes = [
    (86, 3.0),  # G
    (84, 3.375),  # C
    (86, 3.75),  # G (rest on beat 3)
    (81, 4.125),  # Bb
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bass - Walking line in Fm
# Bb, B, C, Db, D, Eb, F, Gb
bass_notes = [
    (58, 3.0),  # Bb
    (59, 3.375),  # B
    (60, 3.75),  # C
    (52, 4.125),  # Db
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano - 7th chords on 2 and 4
# G7 on beat 2 (G, B, D, F)
# C7 on beat 4 (C, E, G, B)
piano_notes = [
    (62, 3.375),  # G
    (67, 3.375),  # B
    (65, 3.375),  # D
    (60, 3.375),  # F
    (60, 4.125),  # C
    (64, 4.125),  # E
    (62, 4.125),  # G
    (67, 4.125),  # B
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Drums - Bar 3
drum_notes = [
    (36, 3.0),  # Kick on 1
    (38, 3.375),  # Snare on 2
    (36, 3.75),  # Kick on 3
    (38, 4.125),  # Snare on 4
    (42, 3.0),  # Hihat on 1
    (42, 3.1875),  # Hihat on 1+
    (42, 3.375),  # Hihat on 2
    (42, 3.5625),  # Hihat on 2+
    (42, 3.75),  # Hihat on 3
    (42, 3.9375),  # Hihat on 3+
    (42, 4.125),  # Hihat on 4
    (42, 4.3125)  # Hihat on 4+
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - Melody: Repeat the motif, but change it again (Bb, D, rest on beat 3, C on beat 4)
sax_notes = [
    (81, 4.5),  # Bb
    (67, 4.875),  # D
    (81, 5.25),  # Bb (rest on beat 3)
    (60, 5.625),  # C
]
for note, time in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375)
    sax.notes.append(sax_note)

# Bass - Walking line in Fm
# D, Eb, F, Gb, G, Ab, A, Bb
bass_notes = [
    (62, 4.5),  # D
    (55, 4.875),  # Eb
    (53, 5.25),  # F
    (52, 5.625),  # Gb
]
for note, time in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375)
    bass.notes.append(bass_note)

# Piano - 7th chords on 2 and 4
# D7 on beat 2 (D, F, A, C)
# G7 on beat 4 (G, B, D, F)
piano_notes = [
    (62, 4.875),  # D
    (60, 4.875),  # F
    (67, 4.875),  # A
    (65, 4.875),  # C
    (62, 5.625),  # G
    (67, 5.625),  # B
    (65, 5.625),  # D
    (60, 5.625),  # F
]
for note, time in piano_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375)
    piano.notes.append(piano_note)

# Drums - Bar 4
drum_notes = [
    (36, 4.5),  # Kick on 1
    (38, 4.875),  # Snare on 2
    (36, 5.25),  # Kick on 3
    (38, 5.625),  # Snare on 4
    (42, 4.5),  # Hihat on 1
    (42, 4.6875),  # Hihat on 1+
    (42, 4.875),  # Hihat on 2
    (42, 5.0625),  # Hihat on 2+
    (42, 5.25),  # Hihat on 3
    (42, 5.4375),  # Hihat on 3+
    (42, 5.625),  # Hihat on 4
    (42, 5.8125)  # Hihat on 4+
]
for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('intro.mid')
