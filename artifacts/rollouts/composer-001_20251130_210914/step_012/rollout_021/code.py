
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),  # D
    (61, 1.875, 0.375), # C
    (63, 2.25, 0.375),  # Eb
    (65, 2.625, 0.375), # F
    (64, 2.8125, 0.375), # E
    (62, 3.1875, 0.375), # D
    (61, 3.5625, 0.375), # C
    (63, 3.9375, 0.375), # Eb
    (65, 4.3125, 0.375), # F
    (64, 4.6875, 0.375), # E
    (62, 5.0625, 0.375), # D
    (61, 5.4375, 0.375), # C
    (63, 5.8125, 0.375)  # Eb
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4 in Dm
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    (62, 1.5, 0.375),  # D
    (67, 1.5, 0.375),  # A
    (64, 1.5, 0.375),  # F
    (69, 1.5, 0.375),  # C
    (67, 2.25, 0.375), # A
    (64, 2.25, 0.375), # F
    (69, 2.25, 0.375), # C
    (66, 2.25, 0.375), # Bb
    # Bar 3 (3.0 - 4.5)
    (62, 3.0, 0.375),  # D
    (67, 3.0, 0.375),  # A
    (64, 3.0, 0.375),  # F
    (69, 3.0, 0.375),  # C
    (67, 3.75, 0.375), # A
    (64, 3.75, 0.375), # F
    (69, 3.75, 0.375), # C
    (66, 3.75, 0.375), # Bb
    # Bar 4 (4.5 - 6.0)
    (62, 4.5, 0.375),  # D
    (67, 4.5, 0.375),  # A
    (64, 4.5, 0.375),  # F
    (69, 4.5, 0.375),  # C
    (67, 5.25, 0.375), # A
    (64, 5.25, 0.375), # F
    (69, 5.25, 0.375), # C
    (66, 5.25, 0.375)  # Bb
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante: Motif on tenor sax - short, singable, ends hanging
sax_notes = [
    (64, 1.5, 0.375),  # E (Dm7)
    (66, 1.875, 0.375), # G
    (62, 2.25, 0.375),  # D
    (64, 2.625, 0.375), # E
    (66, 3.0, 0.375),   # G
    (62, 3.375, 0.375), # D
    (64, 3.75, 0.375),  # E
    (66, 4.125, 0.375), # G
    (62, 4.5, 0.375),   # D
    (64, 4.875, 0.375), # E
    (66, 5.25, 0.375),  # G
    (62, 5.625, 0.375)  # D
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Fill the rest of the drum bar 1 with hihat
for i in range(0, 15):
    hihat_start = 0.0 + i * 0.1875
    if hihat_start < 1.5:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

# Fill the rest of the drum bar 2 with hihat
for i in range(0, 15):
    hihat_start = 1.5 + i * 0.1875
    if hihat_start < 3.0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

# Fill the rest of the drum bar 3 with hihat
for i in range(0, 15):
    hihat_start = 3.0 + i * 0.1875
    if hihat_start < 4.5:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

# Fill the rest of the drum bar 4 with hihat
for i in range(0, 15):
    hihat_start = 4.5 + i * 0.1875
    if hihat_start < 6.0:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=hihat_start, end=hihat_start + 0.1875))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
