
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
    (36, 0.0, 1.0),     # Kick on 1
    (42, 0.0, 0.5),     # Hihat on 1
    (42, 0.5, 1.0),     # Hihat on 2
    (38, 1.0, 1.5),     # Snare on 3
    (42, 1.0, 1.5),     # Hihat on 3
    (42, 1.5, 2.0),     # Hihat on 4
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice.
# F minor walking bass line with chromatic passing tones
bass_notes = [
    (53, 1.5, 1.75),    # F (beat 1)
    (52, 1.75, 2.0),    # Eb (beat 2)
    (51, 2.0, 2.25),    # D (beat 3)
    (53, 2.25, 2.5),    # F (beat 4)
    (54, 2.5, 2.75),    # G (beat 1)
    (55, 2.75, 3.0),    # Ab (beat 2)
    (57, 3.0, 3.25),    # Bb (beat 3)
    (58, 3.25, 3.5),    # B (beat 4)
    (57, 3.5, 3.75),    # Bb (beat 1)
    (56, 3.75, 4.0),    # A (beat 2)
    (54, 4.0, 4.25),    # G (beat 3)
    (53, 4.25, 4.5),    # F (beat 4)
    (51, 4.5, 4.75),    # D (beat 1)
    (52, 4.75, 5.0),    # Eb (beat 2)
    (53, 5.0, 5.25),    # F (beat 3)
    (55, 5.25, 5.5),    # Ab (beat 4)
]
for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Diane: 7th chords, comp on 2 and 4.
# F7 on beat 2, Bb7 on beat 4
piano_notes = [
    # Bar 2
    (59, 1.75, 2.0),    # A on beat 2 (F7)
    (60, 1.75, 2.0),    # Bb
    (62, 1.75, 2.0),    # D
    (64, 1.75, 2.0),    # F
    (67, 1.75, 2.0),    # A
    (69, 1.75, 2.0),    # C
    (71, 1.75, 2.0),    # Eb

    # Bar 3
    (64, 3.25, 3.5),    # F on beat 2 (Bb7)
    (67, 3.25, 3.5),    # A
    (69, 3.25, 3.5),    # C
    (71, 3.25, 3.5),    # Eb
    (74, 3.25, 3.5),    # G
    (76, 3.25, 3.5),    # Bb
    (78, 3.25, 3.5),    # Db

    # Bar 4
    (59, 4.75, 5.0),    # A on beat 2 (F7)
    (60, 4.75, 5.0),    # Bb
    (62, 4.75, 5.0),    # D
    (64, 4.75, 5.0),    # F
    (67, 4.75, 5.0),    # A
    (69, 4.75, 5.0),    # C
    (71, 4.75, 5.0),    # Eb
]
for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
# Bar 2 (1.5 - 3.0)
drum_notes = [
    (36, 1.5, 1.75),    # Kick on 1
    (42, 1.5, 1.75),    # Hihat
    (42, 1.75, 2.0),    # Hihat
    (38, 2.0, 2.25),    # Snare on 2
    (42, 2.0, 2.25),    # Hihat
    (42, 2.25, 2.5),    # Hihat
    (36, 2.5, 2.75),    # Kick on 3
    (42, 2.5, 2.75),    # Hihat
    (42, 2.75, 3.0),    # Hihat
    (38, 3.0, 3.25),    # Snare on 4
    (42, 3.0, 3.25),    # Hihat
    (42, 3.25, 3.5),    # Hihat
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 3 (3.0 - 4.5)
drum_notes = [
    (36, 3.0, 3.25),    # Kick on 1
    (42, 3.0, 3.25),    # Hihat
    (42, 3.25, 3.5),    # Hihat
    (38, 3.5, 3.75),    # Snare on 2
    (42, 3.5, 3.75),    # Hihat
    (42, 3.75, 4.0),    # Hihat
    (36, 4.0, 4.25),    # Kick on 3
    (42, 4.0, 4.25),    # Hihat
    (42, 4.25, 4.5),    # Hihat
    (38, 4.5, 4.75),    # Snare on 4
    (42, 4.5, 4.75),    # Hihat
    (42, 4.75, 5.0),    # Hihat
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 4 (4.5 - 6.0)
drum_notes = [
    (36, 4.5, 4.75),    # Kick on 1
    (42, 4.5, 4.75),    # Hihat
    (42, 4.75, 5.0),    # Hihat
    (38, 5.0, 5.25),    # Snare on 2
    (42, 5.0, 5.25),    # Hihat
    (42, 5.25, 5.5),    # Hihat
    (36, 5.5, 5.75),    # Kick on 3
    (42, 5.5, 5.75),    # Hihat
    (42, 5.75, 6.0),    # Hihat
    (38, 6.0, 6.25),    # Snare on 4
    (42, 6.0, 6.25),    # Hihat
    (42, 6.25, 6.5),    # Hihat
]
for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F minor motif: F - G - Eb - D
sax_notes = [
    (53, 1.5, 1.75),    # F on beat 1
    (55, 1.75, 2.0),    # G on beat 2
    (51, 2.0, 2.25),    # Eb on beat 3
    (50, 2.25, 2.5),    # D on beat 4

    (53, 2.5, 2.75),    # F on beat 1
    (55, 2.75, 3.0),    # G on beat 2
    (51, 3.0, 3.25),    # Eb on beat 3
    (50, 3.25, 3.5),    # D on beat 4

    (53, 3.5, 3.75),    # F on beat 1
    (55, 3.75, 4.0),    # G on beat 2
    (51, 4.0, 4.25),    # Eb on beat 3
    (50, 4.25, 4.5),    # D on beat 4

    (53, 4.5, 4.75),    # F on beat 1
    (55, 4.75, 5.0),    # G on beat 2
    (51, 5.0, 5.25),    # Eb on beat 3
    (50, 5.25, 5.5),    # D on beat 4

    (53, 5.5, 5.75),    # F on beat 1
    (55, 5.75, 6.0),    # G on beat 2
]
for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
