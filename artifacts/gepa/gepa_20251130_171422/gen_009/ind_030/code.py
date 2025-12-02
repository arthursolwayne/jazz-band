
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36  # Kick drum
snare = 38  # Snare drum
hihat = 42  # Hi-hat

# =================== BAR 1: DRUMS ONLY (0.0 - 1.5s) ===================

# Little Ray's intro - groove with space and tension
# Kick on 1 and 3, snare on 2 and 4, hihat every eighth
bar_length = 1.5  # seconds per bar
beat_length = 0.375  # seconds per beat (60 / 160 = 0.375)

# Bar 1: 4 beats
drum_notes = [
    # Kick on 1 and 3
    (kick, 0.0),
    (kick, 1.125),
    # Snare on 2 and 4
    (snare, 0.75),
    (snare, 1.5),
    # Hihat on every eighth
    (hihat, 0.0),
    (hihat, 0.375),
    (hihat, 0.75),
    (hihat, 1.125),
    (hihat, 1.5)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# =================== BAR 2: FULL QUARTET (1.5 - 3.0s) ===================

# Time starts at 1.5s

# DIANE - PIANO: F7 (Fm7 chord), comp on offbeats, angry but supportive
# Fm7 = F, Ab, C, Eb
# Comp on beats 2 and 4 (offbeats)
piano_notes = [
    # Bar 2, beat 2: F7 chord (Ab, C, F, Eb)
    (64, 1.5 + 0.75, 0.25),  # Ab (Fm7 root)
    (60, 1.5 + 0.75, 0.25),  # F
    (62, 1.5 + 0.75, 0.25),  # C
    (61, 1.5 + 0.75, 0.25),  # Eb
    # Bar 2, beat 4: F7 again
    (64, 1.5 + 1.125, 0.25),
    (60, 1.5 + 1.125, 0.25),
    (62, 1.5 + 1.125, 0.25),
    (61, 1.5 + 1.125, 0.25),
]

for note, time, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    piano.notes.append(piano_note)

# MARCUS - BASS: chromatic walk, Fm7 to Bb7, walking the bass line
# Fm7: F, Ab, C, Eb
# Bb7: Bb, D, F, Ab
# Chromatic walk down from F to Bb
bass_notes = [
    (64, 1.5, 0.5),  # F
    (63, 1.5 + 0.375, 0.375),  # E
    (62, 1.5 + 0.75, 0.375),  # D
    (61, 1.5 + 1.125, 0.375),  # C
    (60, 1.5 + 1.5, 0.375),  # Bb
]

for note, time, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + duration)
    bass.notes.append(bass_note)

# DANTÉ - SAX: the motif, short and expressive
# Fm scale: F, Gb, Ab, A, Bb, B, C
# Motif: F (64), Ab (66), Bb (62), C (65)
# Play on beat 1, leave it hanging, come back on beat 3
sax_notes = [
    (64, 1.5, 0.5),  # F
    (66, 1.5 + 0.75, 0.5),  # Ab
    (62, 1.5 + 1.125, 0.5),  # Bb
    (65, 1.5 + 1.5, 0.5),  # C
]

for note, time, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration)
    sax.notes.append(sax_note)

# DRUMS: continue the groove
# Bar 2: Kick on 1 and 3, Snare on 2 and 4, Hihat every eighth
drum_notes = [
    (kick, 1.5),
    (kick, 1.5 + 1.125),
    (snare, 1.5 + 0.75),
    (snare, 1.5 + 1.5),
    (hihat, 1.5),
    (hihat, 1.5 + 0.375),
    (hihat, 1.5 + 0.75),
    (hihat, 1.5 + 1.125),
    (hihat, 1.5 + 1.5)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# =================== BAR 3: FULL QUARTET (3.0 - 4.5s) ===================

# DIANE - PIANO: Back to F7, but with a twist on beat 3
# F7 with chromatic passing tone (Ab -> G -> F)
piano_notes = [
    (64, 3.0, 0.25),  # Ab
    (60, 3.0, 0.25),  # F
    (62, 3.0, 0.25),  # C
    (61, 3.0, 0.25),  # Eb
    (63, 3.0 + 0.75, 0.25),  # G
    (64, 3.0 + 1.125, 0.25),  # Ab
    (60, 3.0 + 1.125, 0.25),  # F
    (62, 3.0 + 1.125, 0.25),  # C
    (61, 3.0 + 1.125, 0.25),  # Eb
]

for note, time, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    piano.notes.append(piano_note)

# MARCUS - BASS: Fm7 to Bb7, walking again
# Fm7: F, Ab, C, Eb
# Bb7: Bb, D, F, Ab
bass_notes = [
    (64, 3.0, 0.5),  # F
    (63, 3.0 + 0.375, 0.375),  # E
    (62, 3.0 + 0.75, 0.375),  # D
    (61, 3.0 + 1.125, 0.375),  # C
    (60, 3.0 + 1.5, 0.375),  # Bb
]

for note, time, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + duration)
    bass.notes.append(bass_note)

# DANTÉ - SAX: Repeat the motif with a slight variation
# Add a half-step chromatic run on the final note
sax_notes = [
    (64, 3.0, 0.5),  # F
    (66, 3.0 + 0.75, 0.5),  # Ab
    (62, 3.0 + 1.125, 0.5),  # Bb
    (65, 3.0 + 1.5, 0.25),  # C
    (66, 3.0 + 1.5, 0.25),  # C#
]

for note, time, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration)
    sax.notes.append(sax_note)

# DRUMS: continue the groove
drum_notes = [
    (kick, 3.0),
    (kick, 3.0 + 1.125),
    (snare, 3.0 + 0.75),
    (snare, 3.0 + 1.5),
    (hihat, 3.0),
    (hihat, 3.0 + 0.375),
    (hihat, 3.0 + 0.75),
    (hihat, 3.0 + 1.125),
    (hihat, 3.0 + 1.5)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# =================== BAR 4: FULL QUARTET (4.5 - 6.0s) ===================

# DIANE - PIANO: Fm7 again, with a new tension on beat 2
piano_notes = [
    (64, 4.5, 0.25),  # Ab
    (60, 4.5, 0.25),  # F
    (62, 4.5, 0.25),  # C
    (61, 4.5, 0.25),  # Eb
    (63, 4.5 + 0.75, 0.25),  # G
    (64, 4.5 + 1.125, 0.25),  # Ab
    (60, 4.5 + 1.125, 0.25),  # F
    (62, 4.5 + 1.125, 0.25),  # C
    (61, 4.5 + 1.125, 0.25),  # Eb
]

for note, time, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration)
    piano.notes.append(piano_note)

# MARCUS - BASS: Fm7 to Bb7, walking again
bass_notes = [
    (64, 4.5, 0.5),  # F
    (63, 4.5 + 0.375, 0.375),  # E
    (62, 4.5 + 0.75, 0.375),  # D
    (61, 4.5 + 1.125, 0.375),  # C
    (60, 4.5 + 1.5, 0.375),  # Bb
]

for note, time, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + duration)
    bass.notes.append(bass_note)

# DANTÉ - SAX: Final variation, let it hang with a subtle resolution
sax_notes = [
    (64, 4.5, 0.5),  # F
    (66, 4.5 + 0.75, 0.5),  # Ab
    (62, 4.5 + 1.125, 0.5),  # Bb
    (65, 4.5 + 1.5, 0.5),  # C
]

for note, time, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + duration)
    sax.notes.append(sax_note)

# DRUMS: final groove
drum_notes = [
    (kick, 4.5),
    (kick, 4.5 + 1.125),
    (snare, 4.5 + 0.75),
    (snare, 4.5 + 1.5),
    (hihat, 4.5),
    (hihat, 4.5 + 0.375),
    (hihat, 4.5 + 0.75),
    (hihat, 4.5 + 1.125),
    (hihat, 4.5 + 1.5)
]

for note, time in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drums.notes.append(drum_note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
