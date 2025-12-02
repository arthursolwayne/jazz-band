
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# BAR 2: Full quartet (1.5 - 3.0s)
# SAX: Start the motif on Fm7 (F, Ab, Bb, D) with a short, angular phrase
sax_notes = [
    (84, 1.5), (80, 1.75), (82, 2.0), (84, 2.25),  # F, Eb, F#, F
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# BASS: Walking line in Fm - F, Gb, Ab, A
bass_notes = [
    (64, 1.5), (63, 1.75), (65, 2.0), (66, 2.25),
    (64, 2.5), (63, 2.75), (65, 3.0), (66, 3.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# PIANO: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2 - F7 (F, A, C, Eb) on beat 2
    (84, 1.75), (87, 1.75), (89, 1.75), (82, 1.75),
    # Bar 2 - Bb7 (Bb, D, F, Ab) on beat 4
    (80, 2.25), (83, 2.25), (84, 2.25), (82, 2.25),
    # Bar 3 - F7 on beat 2
    (84, 2.75), (87, 2.75), (89, 2.75), (82, 2.75),
    # Bar 3 - Bb7 on beat 4
    (80, 3.25), (83, 3.25), (84, 3.25), (82, 3.25),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# BAR 3: Full quartet (3.0 - 4.5s)
# SAX: Repeat motif, starting on Ab (2nd bar of motif)
sax_notes = [
    (82, 3.0), (80, 3.25), (82, 3.5), (84, 3.75),
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# BASS: Walking line in Fm - F, Gb, Ab, A
bass_notes = [
    (64, 3.0), (63, 3.25), (65, 3.5), (66, 3.75),
    (64, 4.0), (63, 4.25), (65, 4.5), (66, 4.75)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# PIANO: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 3 - F7 on beat 2
    (84, 3.25), (87, 3.25), (89, 3.25), (82, 3.25),
    # Bar 3 - Bb7 on beat 4
    (80, 3.75), (83, 3.75), (84, 3.75), (82, 3.75),
    # Bar 4 - F7 on beat 2
    (84, 4.25), (87, 4.25), (89, 4.25), (82, 4.25),
    # Bar 4 - Bb7 on beat 4
    (80, 4.75), (83, 4.75), (84, 4.75), (82, 4.75),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# BAR 4: Full quartet (4.5 - 6.0s)
# SAX: Repeat motif, ending on F (4th bar of motif)
sax_notes = [
    (84, 4.5), (80, 4.75), (82, 5.0), (84, 5.25),
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# BASS: Walking line in Fm - F, Gb, Ab, A
bass_notes = [
    (64, 4.5), (63, 4.75), (65, 5.0), (66, 5.25),
    (64, 5.5), (63, 5.75), (65, 6.0), (66, 6.25)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# PIANO: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 4 - F7 on beat 2
    (84, 4.75), (87, 4.75), (89, 4.75), (82, 4.75),
    # Bar 4 - Bb7 on beat 4
    (80, 5.25), (83, 5.25), (84, 5.25), (82, 5.25),
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    (36, 4.5), (38, 4.875), (42, 4.875),
    (36, 5.25), (38, 5.625), (42, 5.625),
    (36, 6.0), (38, 6.375), (42, 6.375),
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
