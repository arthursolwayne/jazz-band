
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.125),
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125), (42, 1.5, 0.125)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4 (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    (65, 1.5, 0.375), (67, 1.875, 0.375), (64, 2.25, 0.375), (67, 2.625, 0.375),
    (69, 2.875, 0.375), (71, 3.25, 0.375), (70, 3.625, 0.375), (69, 4.0, 0.375),
    (67, 4.375, 0.375), (69, 4.75, 0.375), (71, 5.125, 0.375), (72, 5.5, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    (62, 1.5, 0.375), (67, 1.5, 0.375), (69, 1.5, 0.375), (72, 1.5, 0.375),
    # Bar 3: Bm7 (B-D-F#-A)
    (66, 2.25, 0.375), (69, 2.25, 0.375), (71, 2.25, 0.375), (74, 2.25, 0.375),
    # Bar 4: G7 (G-B-D-F)
    (67, 3.0, 0.375), (71, 3.0, 0.375), (69, 3.0, 0.375), (65, 3.0, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    drum_notes = [
        (36, start, 0.375), (38, start + 0.375, 0.375), (42, start, 0.125),
        (36, start + 1.125, 0.375), (38, start + 1.5, 0.375), (42, start + 1.125, 0.125),
        (42, start + 1.25, 0.125), (42, start + 1.375, 0.125), (42, start + 1.5, 0.125)
    ]
    for note, s, d in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=s, end=s + d))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) - F# (67) - A (69) - D (62) (on beat 1)
# Then leave it hanging on F# (67) on beat 2
# Return on beat 3 to complete the motif

sax_notes = [
    (62, 1.5, 0.375), (67, 1.875, 0.375), (69, 2.25, 0.375), (62, 2.625, 0.375),
    (67, 3.0, 0.375), (69, 3.375, 0.375), (62, 3.75, 0.375)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
