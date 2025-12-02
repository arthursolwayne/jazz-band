
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
drum_notes = [
    (0.0, 36, 100),  # Kick on 1
    (0.75, 42, 80),  # Hihat on & of 1
    (1.0, 38, 100),  # Snare on 2
    (1.5, 36, 100),  # Kick on 3
    (1.75, 42, 80),  # Hihat on & of 3
    (2.0, 38, 100),  # Snare on 4
    (2.25, 42, 80),  # Hihat on & of 4
]

for time, note, velocity in drum_notes:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s) - sax enters with motif
# Dm7 chord: D F A C
# Motif: D -> F -> A -> rest (with slight rhythmic variation)
sax_notes = [
    (1.5, 62, 110),  # D
    (1.75, 65, 110), # F
    (2.0, 69, 110),  # A
    (2.25, 62, 110), # D (slightly late, creating tension)
    (2.5, 65, 110),  # F
    (2.75, 69, 110), # A
    (3.0, 62, 110),  # D
    (3.25, 65, 110), # F
    (3.5, 69, 110),  # A
    (3.75, 0, 0),    # Rest (to leave it hanging)
]

for time, note, velocity in sax_notes:
    if note != 0:
        n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
        sax.notes.append(n)

# Bass: Walking line with chromatic approaches in Dm
# D -> Eb -> F -> G -> A -> Bb -> C -> D
bass_notes = [
    (1.5, 62, 80),   # D
    (1.75, 63, 80),  # Eb
    (2.0, 65, 80),   # F
    (2.25, 67, 80),  # G
    (2.5, 69, 80),   # A
    (2.75, 70, 80),  # Bb
    (3.0, 72, 80),   # C
    (3.25, 69, 80),  # A (chromatic approach)
    (3.5, 67, 80),   # G
    (3.75, 65, 80),  # F
]

for time, note, velocity in bass_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano: Comping on 2 and 4 with 7th chords
# Dm7 = D F A C
piano_notes = [
    (1.75, 62, 80),  # D (2nd beat)
    (1.75, 65, 80),  # F
    (1.75, 69, 80),  # A
    (1.75, 72, 80),  # C
    (2.0, 62, 80),   # D (4th beat)
    (2.0, 65, 80),   # F
    (2.0, 69, 80),   # A
    (2.0, 72, 80),   # C
    (3.25, 62, 80),  # D (2nd beat of bar 3)
    (3.25, 65, 80),  # F
    (3.25, 69, 80),  # A
    (3.25, 72, 80),  # C
    (3.5, 62, 80),   # D (4th beat of bar 3)
    (3.5, 65, 80),   # F
    (3.5, 69, 80),   # A
    (3.5, 72, 80),   # C
]

for time, note, velocity in piano_notes:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 3 (3.0 - 4.5s)
# Drums continue with slight variation
drum_notes_bar3 = [
    (3.0, 36, 100),  # Kick on 1
    (3.75, 42, 80),  # Hihat on & of 1
    (4.0, 38, 100),  # Snare on 2
    (4.5, 36, 100),  # Kick on 3
    (4.75, 42, 80),  # Hihat on & of 3
    (5.0, 38, 100),  # Snare on 4
    (5.25, 42, 80),  # Hihat on & of 4
]

for time, note, velocity in drum_notes_bar3:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Bar 4 (4.5 - 6.0s)
# Sax continues with motif, ends on a question
sax_notes_bar4 = [
    (4.5, 62, 110),  # D
    (4.75, 65, 110), # F
    (5.0, 69, 110),  # A
    (5.25, 64, 110), # Eb (chromatic approach)
    (5.5, 67, 110),  # G
    (5.75, 69, 110), # A
    (6.0, 65, 110),  # F (ends on a question)
]

for time, note, velocity in sax_notes_bar4:
    if note != 0:
        n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
        sax.notes.append(n)

# Bass continues walking line
bass_notes_bar4 = [
    (4.5, 62, 80),   # D
    (4.75, 63, 80),  # Eb
    (5.0, 65, 80),   # F
    (5.25, 67, 80),  # G
    (5.5, 69, 80),   # A
    (5.75, 70, 80),  # Bb
    (6.0, 72, 80),   # C
    (6.25, 69, 80),  # A
]

for time, note, velocity in bass_notes_bar4:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(n)

# Piano continues comping
piano_notes_bar4 = [
    (4.75, 62, 80),  # D
    (4.75, 65, 80),  # F
    (4.75, 69, 80),  # A
    (4.75, 72, 80),  # C
    (5.0, 62, 80),   # D
    (5.0, 65, 80),   # F
    (5.0, 69, 80),   # A
    (5.0, 72, 80),   # C
    (5.75, 62, 80),  # D
    (5.75, 65, 80),  # F
    (5.75, 69, 80),  # A
    (5.75, 72, 80),  # C
]

for time, note, velocity in piano_notes_bar4:
    n = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(n)

# Bar 4 Drums
drum_notes_bar4 = [
    (4.5, 36, 100),  # Kick on 1
    (5.25, 42, 80),  # Hihat on & of 1
    (5.5, 38, 100),  # Snare on 2
    (6.0, 36, 100),  # Kick on 3
    (6.25, 42, 80),  # Hihat on & of 3
    (6.5, 38, 100),  # Snare on 4 (slightly late, creating tension)
    (6.75, 42, 80),  # Hihat on & of 4 (slightly late)
]

for time, note, velocity in drum_notes_bar4:
    dr = pretty_midi.Note(velocity=velocity, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(dr)

# Add instruments to MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
