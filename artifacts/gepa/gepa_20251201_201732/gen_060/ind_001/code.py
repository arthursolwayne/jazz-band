
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in F (D2-G2, MIDI 38-43)
bass_notes = []
bass_time = 1.5
for bar in range(3):
    # Bar starts at 1.5, 3.0, 4.5
    bass_time = 1.5 + bar * 1.5
    # Roots and fifths with chromatic approaches
    # Bar 2: F - G (root and fifth)
    if bar == 0:
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bass_time, end=bass_time + 0.375))  # F
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=bass_time + 0.75, end=bass_time + 1.125))  # G
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bass_time + 1.125, end=bass_time + 1.5))  # Gb chromatic
    # Bar 3: Bb - A (fifth and root of Dm7)
    elif bar == 1:
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=41, start=bass_time, end=bass_time + 0.375))  # Bb
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=40, start=bass_time + 0.75, end=bass_time + 1.125))  # A
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=41, start=bass_time + 1.125, end=bass_time + 1.5))  # Bb chromatic
    # Bar 4: C - B (fifth and root of G7)
    elif bar == 2:
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=39, start=bass_time, end=bass_time + 0.375))  # C
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=43, start=bass_time + 0.75, end=bass_time + 1.125))  # G
        bass_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bass_time + 1.125, end=bass_time + 1.5))  # Gb chromatic
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
piano_notes = []
piano_time = 1.5
for bar in range(3):
    # Bar 2: Fmaj7 (F A C E)
    if bar == 0:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=57, start=piano_time, end=piano_time + 0.75))  # F
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=70, start=piano_time, end=piano_time + 0.75))  # A
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=piano_time, end=piano_time + 0.75))  # C
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=82, start=piano_time, end=piano_time + 0.75))  # E
    # Bar 3: Bbmaj7 (Bb D F A)
    elif bar == 1:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=54, start=piano_time, end=piano_time + 0.75))  # Bb
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=piano_time, end=piano_time + 0.75))  # D
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=piano_time, end=piano_time + 0.75))  # F
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=79, start=piano_time, end=piano_time + 0.75))  # A
    # Bar 4: G7 (G B D F)
    elif bar == 2:
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=67, start=piano_time, end=piano_time + 0.75))  # G
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=79, start=piano_time, end=piano_time + 0.75))  # B
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=piano_time, end=piano_time + 0.75))  # D
        piano_notes.append(pretty_midi.Note(velocity=100, pitch=76, start=piano_time, end=piano_time + 0.75))  # F
    piano_time += 1.5
piano.notes.extend(piano_notes)

# Dante: Sax melody (Bar 2-4)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = []

# Bar 2: Start motif
sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875))  # A (Fmaj7)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25))  # Bb (Fmaj7)

# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # G (Bbmaj7)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75))  # Bb (Bbmaj7)

# Bar 4: Come back and finish it
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))  # Bb (G7)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25))  # C (G7)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625))  # C# (G7)
sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0))  # Bb (G7)

sax.notes.extend(sax_notes)

# Drums for Bars 2-4
for bar in range(3):
    start = 1.5 + bar * 1.5
    # Kick on 1 and 3
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125))  # Snare on 2
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))  # Kick on 3
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875))  # Snare on 4
    # Hihat on every eighth
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75))
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125))
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.5, end=start + 1.875))
    sax_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.875, end=start + 2.25))

drums.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
