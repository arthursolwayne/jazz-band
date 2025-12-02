
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 1.0),   # Kick on beat 1
    (38, 0.5, 1.0),   # Snare on beat 2
    (42, 0.0, 1.0),   # Hihat on beat 1
    (42, 0.25, 1.0),  # Hihat on &1
    (42, 0.5, 1.0),   # Hihat on beat 2
    (42, 0.75, 1.0),  # Hihat on &2
    (42, 1.0, 1.0),   # Hihat on beat 3
    (42, 1.25, 1.0),  # Hihat on &3
    (42, 1.5, 1.0),   # Hihat on beat 4
    (36, 1.0, 1.0),   # Kick on beat 3
    (38, 1.5, 1.0),   # Snare on beat 4
]

for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Dm, chromatic approach to Bb
# Dm = D F A
bass_notes = [
    (62, 1.5, 0.25),  # D
    (60, 1.75, 0.25), # F
    (64, 2.0, 0.25),  # A
    (61, 2.25, 0.25), # Bb (chromatic approach to A)
    (62, 2.5, 0.25),  # D
    (60, 2.75, 0.25), # F
    (64, 3.0, 0.25),  # A
]

for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Piano: 7th chords, comp on beats 2 and 4
# Dm7 = D F A C
piano_notes = [
    (64, 1.75, 0.25), # D
    (67, 1.75, 0.25), # F
    (69, 1.75, 0.25), # A
    (71, 1.75, 0.25), # C
    (64, 2.25, 0.25), # D
    (67, 2.25, 0.25), # F
    (69, 2.25, 0.25), # A
    (71, 2.25, 0.25), # C
]

for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + dur))

# Saxophone: sparse, expressive motif
# Start on D, then F, then A, then back to D on the & of 3
sax_notes = [
    (62, 1.5, 0.25),  # D on beat 1
    (65, 1.75, 0.25), # F on beat 2
    (67, 2.0, 0.25),  # A on beat 3
    (62, 2.25, 0.25), # D on &3
]

for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + dur))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: walking line in Dm, chromatic approach to Bb
bass_notes = [
    (62, 3.0, 0.25),  # D
    (60, 3.25, 0.25), # F
    (64, 3.5, 0.25),  # A
    (61, 3.75, 0.25), # Bb (chromatic approach to A)
    (62, 4.0, 0.25),  # D
    (60, 4.25, 0.25), # F
    (64, 4.5, 0.25),  # A
]

for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Piano: 7th chords, comp on beats 2 and 4
piano_notes = [
    (64, 3.25, 0.25), # D
    (67, 3.25, 0.25), # F
    (69, 3.25, 0.25), # A
    (71, 3.25, 0.25), # C
    (64, 3.75, 0.25), # D
    (67, 3.75, 0.25), # F
    (69, 3.75, 0.25), # A
    (71, 3.75, 0.25), # C
]

for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + dur))

# Saxophone: continue motif, but now with a slight variation
# D -> F -> A -> C, with a slight delay on C
sax_notes = [
    (62, 3.0, 0.25),  # D on beat 1
    (65, 3.25, 0.25), # F on beat 2
    (67, 3.5, 0.25),  # A on beat 3
    (71, 3.75, 0.25), # C on beat 4
]

for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + dur))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line: walking line in Dm, chromatic approach to Bb
bass_notes = [
    (62, 4.5, 0.25),  # D
    (60, 4.75, 0.25), # F
    (64, 5.0, 0.25),  # A
    (61, 5.25, 0.25), # Bb (chromatic approach to A)
    (62, 5.5, 0.25),  # D
    (60, 5.75, 0.25), # F
    (64, 6.0, 0.25),  # A
]

for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Piano: 7th chords, comp on beats 2 and 4
piano_notes = [
    (64, 4.75, 0.25), # D
    (67, 4.75, 0.25), # F
    (69, 4.75, 0.25), # A
    (71, 4.75, 0.25), # C
    (64, 5.25, 0.25), # D
    (67, 5.25, 0.25), # F
    (69, 5.25, 0.25), # A
    (71, 5.25, 0.25), # C
]

for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + dur))

# Saxophone: return to the original motif, but with a slight variation
# D -> F -> A -> D, ending on a sustained D
sax_notes = [
    (62, 4.5, 0.25),  # D on beat 1
    (65, 4.75, 0.25), # F on beat 2
    (67, 5.0, 0.25),  # A on beat 3
    (62, 5.25, 0.75), # D on beat 4, held for a little longer
]

for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + dur))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 1.0),   # Kick on beat 1
    (38, 5.0, 1.0),   # Snare on beat 2
    (42, 4.5, 1.0),   # Hihat on beat 1
    (42, 4.75, 1.0),  # Hihat on &1
    (42, 5.0, 1.0),   # Hihat on beat 2
    (42, 5.25, 1.0),  # Hihat on &2
    (42, 5.5, 1.0),   # Hihat on beat 3
    (42, 5.75, 1.0),  # Hihat on &3
    (42, 6.0, 1.0),   # Hihat on beat 4
    (36, 5.5, 1.0),   # Kick on beat 3
    (38, 6.0, 1.0),   # Snare on beat 4
]

for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
