
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.375, 0.125),   # Hihat on &1
    (38, 0.75, 0.375),    # Snare on 2
    (42, 0.875, 0.125),   # Hihat on &2
    (36, 1.125, 0.375),   # Kick on 3
    (42, 1.5, 0.125)      # Hihat on &3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass - Walking line in Dm
bass_notes = [
    (62, 1.5, 0.375),     # D
    (60, 1.875, 0.375),   # Bb
    (63, 2.25, 0.375),    # Eb
    (62, 2.625, 0.375),   # D
    (60, 2.625, 0.375),   # Bb
    (61, 2.625, 0.375),   # C
    (62, 2.625, 0.375),   # D
    (64, 3.0, 0.375)      # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 & 4
piano_notes = [
    (62, 1.875, 0.125),   # D7 chord (D, F#, A, C)
    (64, 1.875, 0.125),
    (67, 1.875, 0.125),
    (69, 1.875, 0.125),
    (62, 3.0, 0.125),
    (64, 3.0, 0.125),
    (67, 3.0, 0.125),
    (69, 3.0, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax - Melody: Whisper to cry
sax_notes = [
    (62, 1.5, 0.375),     # D
    (64, 1.875, 0.375),   # F
    (67, 2.25, 0.375),    # A
    (69, 2.625, 0.375),   # C
    (67, 2.625, 0.375),   # A
    (69, 2.625, 0.375),   # C
    (67, 2.625, 0.375),   # A
    (64, 3.0, 0.375)      # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue in bar 2-4
drum_notes = [
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.375, 0.125),   # Hihat on &1
    (38, 3.75, 0.375),    # Snare on 2
    (42, 3.875, 0.125),   # Hihat on &2
    (36, 4.125, 0.375),   # Kick on 3
    (42, 4.5, 0.125),     # Hihat on &3
    (36, 4.875, 0.375),   # Kick on 1
    (42, 5.25, 0.125),    # Hihat on &1
    (38, 5.625, 0.375),   # Snare on 2
    (42, 5.75, 0.125),    # Hihat on &2
    (36, 6.0, 0.375)      # Kick on 3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3 and 4: Continue bass, piano, and drums
# Bass - continue walking line
bass_notes = [
    (62, 3.0, 0.375),     # D
    (60, 3.375, 0.375),   # Bb
    (63, 3.75, 0.375),    # Eb
    (62, 4.125, 0.375),   # D
    (60, 4.5, 0.375),     # Bb
    (61, 4.875, 0.375),   # C
    (62, 5.25, 0.375),    # D
    (64, 5.625, 0.375)    # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano - 7th chords on 2 & 4
piano_notes = [
    (62, 3.375, 0.125),   # D7 chord
    (64, 3.375, 0.125),
    (67, 3.375, 0.125),
    (69, 3.375, 0.125),
    (62, 5.625, 0.125),
    (64, 5.625, 0.125),
    (67, 5.625, 0.125),
    (69, 5.625, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax - Continue melody
sax_notes = [
    (62, 3.0, 0.375),     # D
    (64, 3.375, 0.375),   # F
    (67, 3.75, 0.375),    # A
    (69, 4.125, 0.375),   # C
    (67, 4.125, 0.375),   # A
    (69, 4.125, 0.375),   # C
    (67, 4.125, 0.375),   # A
    (64, 4.5, 0.375),     # F
    (62, 4.875, 0.375),   # D
    (64, 5.25, 0.375),    # F
    (67, 5.625, 0.375),   # A
    (69, 6.0, 0.375)      # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
