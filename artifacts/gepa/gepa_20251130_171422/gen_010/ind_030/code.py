
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),  # G (1st beat)
    (46, 1.875, 0.375), # Ab (2nd beat)
    (47, 2.25, 0.375),  # Bb (3rd beat)
    (49, 2.625, 0.375), # C (4th beat)
    (50, 3.0, 0.375),   # C# (1st beat)
    (51, 3.375, 0.375), # D (2nd beat)
    (53, 3.75, 0.375),  # Eb (3rd beat)
    (55, 4.125, 0.375), # F (4th beat)
    (56, 4.5, 0.375),   # F# (1st beat)
    (57, 4.875, 0.375), # G (2nd beat)
    (59, 5.25, 0.375),  # A (3rd beat)
    (60, 5.625, 0.375)  # A# (4th beat)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (60, 1.5, 0.375),  # F7 (F, A, C, Eb)
    (62, 1.5, 0.375),
    (65, 1.5, 0.375),
    (67, 1.5, 0.375),
    (62, 1.875, 0.375),  # F7 on beat 2
    (65, 1.875, 0.375),
    (67, 1.875, 0.375),
    (70, 1.875, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (60, 3.0, 0.375),  # F7 (F, A, C, Eb)
    (62, 3.0, 0.375),
    (65, 3.0, 0.375),
    (67, 3.0, 0.375),
    (62, 3.375, 0.375),  # F7 on beat 2
    (65, 3.375, 0.375),
    (67, 3.375, 0.375),
    (70, 3.375, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (60, 4.5, 0.375),  # F7 (F, A, C, Eb)
    (62, 4.5, 0.375),
    (65, 4.5, 0.375),
    (67, 4.5, 0.375),
    (62, 4.875, 0.375),  # F7 on beat 2
    (65, 4.875, 0.375),
    (67, 4.875, 0.375),
    (70, 4.875, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif in F (F, G#, Bb, A) - start it, leave it hanging, come back and finish it
sax_notes = [
    (60, 1.5, 0.375),  # F
    (63, 1.875, 0.375), # G#
    (67, 2.25, 0.375),  # Bb
    (66, 2.625, 0.375), # A
    (60, 3.0, 0.375),  # F (return)
    (63, 3.375, 0.375), # G#
    (67, 3.75, 0.375),  # Bb
    (66, 4.125, 0.375), # A
    (60, 4.5, 0.375),  # F
    (63, 4.875, 0.375), # G#
    (67, 5.25, 0.375),  # Bb
    (66, 5.625, 0.375)  # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = 1.5 * bar
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
