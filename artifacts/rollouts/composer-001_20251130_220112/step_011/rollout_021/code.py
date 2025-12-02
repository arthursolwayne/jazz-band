
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375), (63, 1.875, 0.375), (60, 2.25, 0.375), (62, 2.625, 0.375),
    # Bar 3
    (63, 3.0, 0.375), (60, 3.375, 0.375), (62, 3.75, 0.375), (63, 4.125, 0.375),
    # Bar 4
    (60, 4.5, 0.375), (62, 4.875, 0.375), (63, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, Dm7, F7, Bb7, Cm7, with comping
piano_notes = [
    # Bar 2
    (62, 1.875, 0.1875), (67, 1.875, 0.1875), (65, 1.875, 0.1875), (69, 1.875, 0.1875),
    (65, 2.625, 0.1875), (69, 2.625, 0.1875), (71, 2.625, 0.1875), (74, 2.625, 0.1875),
    # Bar 3
    (62, 3.375, 0.1875), (67, 3.375, 0.1875), (65, 3.375, 0.1875), (69, 3.375, 0.1875),
    (65, 4.125, 0.1875), (69, 4.125, 0.1875), (71, 4.125, 0.1875), (74, 4.125, 0.1875),
    # Bar 4
    (62, 4.875, 0.1875), (67, 4.875, 0.1875), (65, 4.875, 0.1875), (69, 4.875, 0.1875),
    (65, 5.625, 0.1875), (69, 5.625, 0.1875), (71, 5.625, 0.1875), (74, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Melody in Dm, short motif, leave it hanging, then come back
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (62, 2.25, 0.375),
    (65, 3.75, 0.375), (67, 4.125, 0.375), (65, 4.5, 0.375),
    (62, 5.25, 0.375), (65, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.1875, end=start + 0.375)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.5625, end=start + 0.75)
    hihat5 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375)
    hihat6 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.9375, end=start + 1.125)
    hihat7 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125)
    hihat8 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.3125, end=start + 1.5)
    
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4, hihat5, hihat6, hihat7, hihat8])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
