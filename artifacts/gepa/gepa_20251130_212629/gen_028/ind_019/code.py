
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),   # kick on 1
    (42, 0.0, 0.125),   # hihat on 1
    (42, 0.125, 0.125), # hihat on &1
    (38, 0.375, 0.375), # snare on 2
    (42, 0.375, 0.125), # hihat on 2
    (42, 0.5, 0.125),   # hihat on &2
    (36, 0.75, 0.375),  # kick on 3
    (42, 0.75, 0.125),  # hihat on 3
    (42, 0.875, 0.125), # hihat on &3
    (38, 1.125, 0.375), # snare on 4
    (42, 1.125, 0.125), # hihat on 4
    (42, 1.25, 0.125),  # hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),  # D (beat 1)
    (63, 1.875, 0.375), # Eb (beat 2)
    (64, 2.25, 0.375),  # E (beat 3)
    (65, 2.625, 0.375), # F (beat 4)
    (67, 2.625, 0.375), # G (beat 4)
    (69, 3.0, 0.375),   # A (beat 1)
    (70, 3.375, 0.375), # Bb (beat 2)
    (71, 3.75, 0.375),  # B (beat 3)
    (72, 4.125, 0.375), # C (beat 4)
    (74, 4.125, 0.375), # D (beat 4)
    (76, 4.5, 0.375),   # E (beat 1)
    (77, 4.875, 0.375), # F (beat 2)
    (78, 5.25, 0.375),  # G (beat 3)
    (80, 5.625, 0.375), # A (beat 4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.5, 0.375),  # D7 (D, F#, A, C)
    (69, 1.5, 0.375),
    (67, 1.5, 0.375),
    (64, 1.5, 0.375),
    (69, 1.875, 0.375), # Bb7 (Bb, D, F, Ab)
    (76, 1.875, 0.375),
    (74, 1.875, 0.375),
    (71, 1.875, 0.375),
    (62, 2.25, 0.375),  # D7 (D, F#, A, C)
    (69, 2.25, 0.375),
    (67, 2.25, 0.375),
    (64, 2.25, 0.375),
    (69, 2.625, 0.375), # Bb7 (Bb, D, F, Ab)
    (76, 2.625, 0.375),
    (74, 2.625, 0.375),
    (71, 2.625, 0.375),
    (62, 3.0, 0.375),   # D7 (D, F#, A, C)
    (69, 3.0, 0.375),
    (67, 3.0, 0.375),
    (64, 3.0, 0.375),
    (69, 3.375, 0.375), # Bb7 (Bb, D, F, Ab)
    (76, 3.375, 0.375),
    (74, 3.375, 0.375),
    (71, 3.375, 0.375),
    (62, 3.75, 0.375),  # D7 (D, F#, A, C)
    (69, 3.75, 0.375),
    (67, 3.75, 0.375),
    (64, 3.75, 0.375),
    (69, 4.125, 0.375), # Bb7 (Bb, D, F, Ab)
    (76, 4.125, 0.375),
    (74, 4.125, 0.375),
    (71, 4.125, 0.375),
    (62, 4.5, 0.375),   # D7 (D, F#, A, C)
    (69, 4.5, 0.375),
    (67, 4.5, 0.375),
    (64, 4.5, 0.375),
    (69, 4.875, 0.375), # Bb7 (Bb, D, F, Ab)
    (76, 4.875, 0.375),
    (74, 4.875, 0.375),
    (71, 4.875, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), A (69), D (62) - but space it out, use rests, no scale runs
sax_notes = [
    (62, 1.5, 0.375),  # D on beat 1
    (67, 1.875, 0.375), # F# on beat 2
    (69, 2.25, 0.375),  # A on beat 3
    (62, 3.0, 0.375),   # D on beat 4
    (62, 4.5, 0.375),   # D on beat 1 of bar 3
    (67, 4.875, 0.375), # F# on beat 2 of bar 3
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add expression to sax
for note in sax.notes:
    note.velocity = 110
    note.pitch = note.pitch

# Add dynamics to piano
for note in piano.notes:
    note.velocity = 100 + (note.start % 2)*20

# Add dynamics to bass
for note in bass.notes:
    note.velocity = 80 + (note.start % 2)*10

# Add dynamics to drums
for note in drums.notes:
    note.velocity = 100

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
