
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
    (36, 0.0, 0.5),  # Kick on 1
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.5),  # Snare on 2
    (42, 0.875, 0.125),  # Hihat on &2
    (36, 1.125, 0.5),  # Kick on 3
    (42, 1.5, 0.125)   # Hihat on &3
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line
bass_notes = [
    (53, 1.5, 0.25),   # F (root)
    (51, 1.75, 0.25),  # Eb (chromatic approach)
    (53, 2.0, 0.25),   # F
    (55, 2.25, 0.25)   # G (chromatic)
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comp: 7th chords, on 2 and 4
piano_notes = [
    # Bar 2: On beat 2 (1.75s)
    (60, 1.75, 0.25),   # C7: C (60)
    (64, 1.75, 0.25),   # E (64)
    (67, 1.75, 0.25),   # G (67)
    (69, 1.75, 0.25),   # Bb (69)
    
    # Bar 2: On beat 4 (2.25s)
    (60, 2.25, 0.25),   # C7
    (64, 2.25, 0.25),
    (67, 2.25, 0.25),
    (69, 2.25, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax melody (bar 2, starting on beat 1)
sax_notes = [
    (62, 1.5, 0.25),   # D (start of motif)
    (64, 1.75, 0.25),  # E
    (62, 2.0, 0.1),   # D (short rest, hanging)
    (62, 2.1, 0.3)    # D (resolve with anticipation)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line
bass_notes = [
    (55, 3.0, 0.25),   # G
    (53, 3.25, 0.25),  # F
    (50, 3.5, 0.25),   # D (chromatic approach)
    (53, 3.75, 0.25)   # F
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: On beat 2 (3.25s)
    (60, 3.25, 0.25),
    (64, 3.25, 0.25),
    (67, 3.25, 0.25),
    (69, 3.25, 0.25),
    
    # Bar 3: On beat 4 (3.75s)
    (60, 3.75, 0.25),
    (64, 3.75, 0.25),
    (67, 3.75, 0.25),
    (69, 3.75, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax (Bar 3)
sax_notes = [
    (62, 3.0, 0.25),   # D (motif again)
    (64, 3.25, 0.25),  # E
    (62, 3.5, 0.1),   # D (rest)
    (62, 3.6, 0.3)    # D (end with question)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line
bass_notes = [
    (53, 4.5, 0.25),   # F
    (51, 4.75, 0.25),  # Eb
    (53, 5.0, 0.25),   # F
    (55, 5.25, 0.25)   # G
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: On beat 2 (4.75s)
    (60, 4.75, 0.25),
    (64, 4.75, 0.25),
    (67, 4.75, 0.25),
    (69, 4.75, 0.25),
    
    # Bar 4: On beat 4 (5.25s)
    (60, 5.25, 0.25),
    (64, 5.25, 0.25),
    (67, 5.25, 0.25),
    (69, 5.25, 0.25)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Sax (Bar 4)
sax_notes = [
    (62, 4.5, 0.25),   # D (motif again)
    (64, 4.75, 0.25),  # E
    (62, 5.0, 0.1),   # D (rest)
    (62, 5.1, 0.3)    # D (end with question)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Full pattern
drum_notes = [
    # Bar 3
    (36, 3.0, 0.5),    # Kick on 1
    (42, 3.375, 0.125),  # Hihat on &1
    (38, 3.75, 0.5),   # Snare on 2
    (42, 3.875, 0.125),  # Hihat on &2
    (36, 4.125, 0.5),  # Kick on 3
    (42, 4.5, 0.125),  # Hihat on &3

    # Bar 4
    (36, 4.5, 0.5),    # Kick on 1
    (42, 4.875, 0.125),  # Hihat on &1
    (38, 5.25, 0.5),   # Snare on 2
    (42, 5.375, 0.125),  # Hihat on &2
    (36, 5.625, 0.5),  # Kick on 3
    (42, 6.0, 0.125)   # Hihat on &3
]
for note, start, duration in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
