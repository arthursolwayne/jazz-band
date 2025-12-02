
import pretty_midi

# Create a new MIDI file with tempo 160 BPM (Quarter note = 0.75s)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# MIDI note numbers for Dm7 chord: D (62), F (64), A (69), C (60)
# Time signatures: 4/4, 160 BPM, so each beat = 0.75 seconds, bar = 3 seconds

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

drum_notes = [
    (36, 0.0),      # Kick on beat 1
    (42, 0.375),    # Hihat on beat 1 & 2
    (38, 0.75),     # Snare on beat 2
    (42, 1.125),    # Hihat
    (36, 1.5),      # Kick on beat 3
    (42, 1.875),    # Hihat
    (38, 2.25),     # Snare on beat 4
    (42, 2.625)     # Hihat
]

for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.125)
    drums.notes.append(note)

# BAR 2: Full quartet (1.5 - 3.0s)
# Sax: Melody - Dm (D, F, A, C) with a short motif (D -> F -> Bb -> D)
# Bass: Walking line with chromatic approaches
# Piano: Comp on 2 and 4 with 7th chords
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Saxophone Melody
sax_notes = [
    (62, 1.5),      # D
    (64, 1.875),    # F
    (66, 2.25),     # Bb
    (62, 2.625)     # D
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bass Line: Dm walking line with chromatic approaches
bass_notes = [
    (60, 1.5),      # C (chromatic approach to D)
    (62, 1.875),    # D
    (63, 2.25),     # D#
    (64, 2.625)     # F
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano Comp: Dm7 on beat 2 and 4
piano_notes = [
    (62, 1.875),    # D
    (64, 1.875),    # F
    (69, 1.875),    # A
    (60, 1.875),    # C
    (62, 2.625),    # D
    (64, 2.625),    # F
    (69, 2.625),    # A
    (60, 2.625)     # C
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Drums continue for the full bar
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time + 1.5, end=time + 1.625)
    drums.notes.append(note)

# BAR 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but end on Bb (create tension)
# Bass: Continue the walking line
# Piano: Comp on 2 and 4
# Drums: Same pattern

# Saxophone Melody (same motif, but ends on Bb)
sax_notes = [
    (62, 3.0),      # D
    (64, 3.375),    # F
    (66, 3.75),     # Bb
    (66, 4.125)     # Bb (hold)
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bass Line: Continue the walking line
bass_notes = [
    (65, 3.0),      # E
    (62, 3.375),    # D
    (60, 3.75),     # C
    (62, 4.125)     # D
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano Comp: Dm7 on beat 2 and 4
piano_notes = [
    (62, 3.375),    # D
    (64, 3.375),    # F
    (69, 3.375),    # A
    (60, 3.375),    # C
    (62, 4.125),    # D
    (64, 4.125),    # F
    (69, 4.125),    # A
    (60, 4.125)     # C
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Drums continue
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time + 3.0, end=time + 3.125)
    drums.notes.append(note)

# BAR 4: Full quartet (4.5 - 6.0s)
# Sax: Resolution to C (resolve the tension)
# Bass: Walking line
# Piano: Comp on 2 and 4
# Drums: Same pattern

# Saxophone Melody: Resolve to C
sax_notes = [
    (62, 4.5),      # D
    (60, 4.875),    # C
    (62, 5.25),     # D
    (60, 5.625)     # C
]
for note_number, time in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time, end=time + 0.375)
    sax.notes.append(note)

# Bass Line: Continue the walking line
bass_notes = [
    (64, 4.5),      # F
    (65, 4.875),    # E
    (62, 5.25),     # D
    (60, 5.625)     # C
]
for note_number, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note_number, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano Comp: Dm7 on beat 2 and 4
piano_notes = [
    (62, 4.875),    # D
    (64, 4.875),    # F
    (69, 4.875),    # A
    (60, 4.875),    # C
    (62, 5.625),    # D
    (64, 5.625),    # F
    (69, 5.625),    # A
    (60, 5.625)     # C
]
for note_number, time in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note_number, start=time, end=time + 0.375)
    piano.notes.append(note)

# Drums continue
for note_number, time in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note_number, start=time + 4.5, end=time + 4.625)
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
