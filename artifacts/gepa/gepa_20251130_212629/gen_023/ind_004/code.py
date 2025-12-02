
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
    (36, 0.0, 0.375),  # kick on beat 1
    (38, 0.75, 0.375), # snare on beat 2
    (42, 0.0, 0.1875), # hihat on beat 1
    (42, 0.1875, 0.1875), # hihat on &1
    (42, 0.375, 0.1875), # hihat on beat 2
    (42, 0.5625, 0.1875), # hihat on &2
    (36, 1.125, 0.375),  # kick on beat 3
    (38, 1.5, 0.375),   # snare on beat 4
    (42, 1.125, 0.1875), # hihat on beat 3
    (42, 1.3125, 0.1875), # hihat on &3
    (42, 1.5, 0.1875),  # hihat on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line, chromatic approach to Bb
bass_notes = [
    (64, 1.5, 0.375),  # F
    (65, 1.875, 0.375), # Gb
    (66, 2.25, 0.375),  # G
    (64, 2.625, 0.375), # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.875, 0.375), # Bb7 (Bb, D, F, Ab)
    (62, 1.875, 0.375),
    (65, 1.875, 0.375),
    (67, 1.875, 0.375),
    (60, 2.625, 0.375),
    (62, 2.625, 0.375),
    (65, 2.625, 0.375),
    (67, 2.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Start the motif (F, Ab, Bb, rest)
sax_notes = [
    (64, 1.5, 0.375),  # F
    (67, 1.875, 0.375), # Ab
    (66, 2.25, 0.375),  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line, chromatic approach to Eb
bass_notes = [
    (62, 3.0, 0.375),  # Eb
    (63, 3.375, 0.375), # F
    (64, 3.75, 0.375),  # F#
    (62, 4.125, 0.375), # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 3.375, 0.375), # Bb7
    (62, 3.375, 0.375),
    (65, 3.375, 0.375),
    (67, 3.375, 0.375),
    (60, 4.125, 0.375),
    (62, 4.125, 0.375),
    (65, 4.125, 0.375),
    (67, 4.125, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: Continue the motif (rest, Ab, Bb, rest)
sax_notes = [
    (67, 3.375, 0.375),  # Ab
    (66, 3.75, 0.375),   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line, chromatic approach to Ab
bass_notes = [
    (67, 4.5, 0.375),  # Ab
    (68, 4.875, 0.375), # Bb
    (69, 5.25, 0.375),  # B
    (67, 5.625, 0.375), # Ab
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 4.875, 0.375), # Bb7
    (62, 4.875, 0.375),
    (65, 4.875, 0.375),
    (67, 4.875, 0.375),
    (60, 5.625, 0.375),
    (62, 5.625, 0.375),
    (65, 5.625, 0.375),
    (67, 5.625, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Sax: End the motif (rest, F, Ab, rest) — leave it hanging
sax_notes = [
    (64, 5.25, 0.375),  # F
    (67, 5.625, 0.375), # Ab
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # kick on beat 1
    (38, 5.25, 0.375), # snare on beat 2
    (42, 4.5, 0.1875), # hihat on beat 1
    (42, 4.6875, 0.1875), # hihat on &1
    (42, 4.875, 0.1875), # hihat on beat 2
    (42, 5.0625, 0.1875), # hihat on &2
    (36, 5.625, 0.375),  # kick on beat 3
    (38, 6.0, 0.375),   # snare on beat 4
    (42, 5.625, 0.1875), # hihat on beat 3
    (42, 5.8125, 0.1875), # hihat on &3
    (42, 6.0, 0.1875),  # hihat on beat 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
