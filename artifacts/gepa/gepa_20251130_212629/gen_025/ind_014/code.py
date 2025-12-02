
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1& 
    (42, 0.1875, 0.1875), # Hihat on 2
    (38, 0.1875, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2&
    (42, 0.5625, 0.1875), # Hihat on 3
    (36, 0.5625, 0.375), # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3&
    (42, 0.9375, 0.1875), # Hihat on 4
    (38, 0.9375, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4&
    (42, 1.3125, 0.1875) # Hihat on end
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start a motif, leave it hanging

# Dm7 = D F A C
sax_notes = [
    (62, 1.5, 0.375),   # D
    (65, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # A
    (69, 2.625, 0.1875) # C (short, hanging)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm
bass_notes = [
    (50, 1.5, 0.375),   # D
    (52, 1.875, 0.375), # Eb
    (53, 2.25, 0.375),  # F
    (55, 2.625, 0.375)  # G
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 1.875, 0.1875), # D7 on 2
    (64, 1.875, 0.1875), # F
    (67, 1.875, 0.1875), # A
    (71, 1.875, 0.1875), # C
    (62, 2.625, 0.1875), # D7 on 4
    (64, 2.625, 0.1875), # F
    (67, 2.625, 0.1875), # A
    (71, 2.625, 0.1875)  # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but end on a rest
sax_notes = [
    (62, 3.0, 0.375),   # D
    (65, 3.375, 0.375), # F
    (67, 3.75, 0.375),  # A
    (69, 4.125, 0.1875) # C (short, hanging)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm
bass_notes = [
    (57, 3.0, 0.375),   # Bb
    (59, 3.375, 0.375), # B
    (60, 3.75, 0.375),  # C
    (62, 4.125, 0.375)  # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 3.375, 0.1875), # D7 on 2
    (64, 3.375, 0.1875), # F
    (67, 3.375, 0.1875), # A
    (71, 3.375, 0.1875), # C
    (62, 4.125, 0.1875), # D7 on 4
    (64, 4.125, 0.1875), # F
    (67, 4.125, 0.1875), # A
    (71, 4.125, 0.1875)  # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat the motif, but end on a rest
sax_notes = [
    (62, 4.5, 0.375),   # D
    (65, 4.875, 0.375), # F
    (67, 5.25, 0.375),  # A
    (69, 5.625, 0.1875) # C (short, hanging)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Dm
bass_notes = [
    (57, 4.5, 0.375),   # Bb
    (59, 4.875, 0.375), # B
    (60, 5.25, 0.375),  # C
    (62, 5.625, 0.375)  # D
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 4.875, 0.1875), # D7 on 2
    (64, 4.875, 0.1875), # F
    (67, 4.875, 0.1875), # A
    (71, 4.875, 0.1875), # C
    (62, 5.625, 0.1875), # D7 on 4
    (64, 5.625, 0.1875), # F
    (67, 5.625, 0.1875), # A
    (71, 5.625, 0.1875)  # C
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=start, end=start + duration))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1& 
    (42, 4.6875, 0.1875), # Hihat on 2
    (38, 4.6875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2&
    (42, 5.0625, 0.1875), # Hihat on 3
    (36, 5.0625, 0.375), # Kick on 3
    (42, 5.25, 0.1875),  # Hihat on 3&
    (42, 5.4375, 0.1875), # Hihat on 4
    (38, 5.4375, 0.375), # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4&
    (42, 5.8125, 0.1875) # Hihat on end
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
