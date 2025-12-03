
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.375, 0.125),  # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125),  # Hihat on &2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.5, 0.125)     # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) on beat 1, F2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, C3 (MIDI 48) on beat 4
bass_notes = [
    (38, 1.5, 0.375),  # D2 on 1
    (41, 2.0, 0.375),  # F2 on 2
    (45, 2.5, 0.375),  # A2 on 3
    (48, 3.0, 0.375)   # C3 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, D, G)
piano_notes = [
    (62, 1.5, 0.125),  # F
    (67, 1.5, 0.125),  # A
    (64, 1.5, 0.125),  # D
    (71, 1.5, 0.125)   # G
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Short motif, start it, leave it hanging
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375) # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) on beat 1, F2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, C3 (MIDI 48) on beat 4
bass_notes = [
    (38, 3.0, 0.375),  # D2 on 1
    (41, 3.5, 0.375),  # F2 on 2
    (45, 4.0, 0.375),  # A2 on 3
    (48, 4.5, 0.375)   # C3 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Secondary chord (Bbm7) (D, F, Ab, Bb)
piano_notes = [
    (62, 3.0, 0.125),  # D
    (67, 3.0, 0.125),  # F
    (69, 3.0, 0.125),  # Ab
    (71, 3.0, 0.125)   # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.375, 0.125),  # Hihat on &1
    (38, 3.75, 0.375),  # Snare on 2
    (42, 3.875, 0.125),  # Hihat on &2
    (36, 4.125, 0.375),  # Kick on 3
    (42, 4.5, 0.125)     # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) on beat 1, F2 (MIDI 41) on beat 2, A2 (MIDI 45) on beat 3, C3 (MIDI 48) on beat 4
bass_notes = [
    (38, 4.5, 0.375),  # D2 on 1
    (41, 5.0, 0.375),  # F2 on 2
    (45, 5.5, 0.375),  # A2 on 3
    (48, 6.0, 0.375)   # C3 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Return to Dm7 (F, A, D, G)
piano_notes = [
    (62, 4.5, 0.125),  # F
    (67, 4.5, 0.125),  # A
    (64, 4.5, 0.125),  # D
    (71, 4.5, 0.125)   # G
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.875, 0.125),  # Hihat on &1
    (38, 5.25, 0.375),  # Snare on 2
    (42, 5.375, 0.125),  # Hihat on &2
    (36, 5.625, 0.375),  # Kick on 3
    (42, 6.0, 0.125)     # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Return to motif and finish it
sax_notes = [
    (62, 4.5, 0.375),  # D
    (65, 4.875, 0.375),  # F
    (67, 5.25, 0.375)   # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
