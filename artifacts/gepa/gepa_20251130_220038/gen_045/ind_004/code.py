
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
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &
    (42, 1.125, 0.1875), # Hihat on 4
    (36, 1.5, 0.375)    # Kick on 3
]

for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line with chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (64, 2.25, 0.375),  # E
    (65, 2.625, 0.375), # F
    (67, 3.0, 0.375),   # G
    (69, 3.375, 0.375), # A
    (71, 3.75, 0.375),  # Bb
    (72, 4.125, 0.375), # B
    (74, 4.5, 0.375),   # C
    (76, 4.875, 0.375), # D
    (77, 5.25, 0.375),  # Eb
    (79, 5.625, 0.375)  # F
]

for note, start, dur in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + dur))

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2
    (67, 2.25, 0.375), # G
    (72, 2.25, 0.375), # B
    (65, 2.25, 0.375), # F
    (74, 2.25, 0.375), # C
    # Bar 3: D7 on 2
    (67, 3.75, 0.375), # G
    (72, 3.75, 0.375), # B
    (65, 3.75, 0.375), # F
    (74, 3.75, 0.375), # C
    # Bar 4: D7 on 2
    (67, 5.25, 0.375), # G
    (72, 5.25, 0.375), # B
    (65, 5.25, 0.375), # F
    (74, 5.25, 0.375)  # C
]

for note, start, dur in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + dur))

# Sax: Dante - A whisper at first, then a cry
# Start with a short motif, leave it hanging, then come back and finish it
# D - F - G - Bb (whispered)
# Then a cry: D - Bb - G - D
sax_notes = [
    (62, 1.5, 0.375),   # D
    (64, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # G
    (69, 2.625, 0.375), # Bb
    (62, 3.0, 0.375),   # D
    (69, 3.375, 0.375), # Bb
    (67, 3.75, 0.375),  # G
    (62, 4.125, 0.375)  # D
]

for note, start, dur in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

# Drums: Fill the bar with hihat and kick/snare on 1 and 3
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (38, 2.25, 0.375),  # Snare on 2
    (42, 1.5, 0.1875),  # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on &
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875), # Hihat on &
    (42, 2.25, 0.1875), # Hihat on 3
    (42, 2.4375, 0.1875), # Hihat on &
    (42, 2.625, 0.1875), # Hihat on 4
    (36, 3.0, 0.375),   # Kick on 1
    (38, 3.75, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &
    (42, 4.125, 0.1875), # Hihat on 4
    (36, 4.5, 0.375),   # Kick on 1
    (38, 5.25, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &
    (42, 5.625, 0.1875)  # Hihat on 4
]

for note, start, dur in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + dur))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
