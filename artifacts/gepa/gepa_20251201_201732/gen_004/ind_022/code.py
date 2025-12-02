
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass: Walking line with chromatic approaches
# D2 (D) to G2 (G), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (D), chromatic approach to G
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D2
    pretty_midi.Note(velocity=75, pitch=39, start=1.875, end=2.0), # chromatic
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.375), # G2

    # Bar 3: G2 (G), chromatic approach to A
    pretty_midi.Note(velocity=80, pitch=43, start=2.375, end=2.75), # G2
    pretty_midi.Note(velocity=75, pitch=44, start=2.75, end=3.0), # chromatic
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375), # A2

    # Bar 4: A2 (A), chromatic approach to D
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=75, pitch=46, start=3.75, end=4.0), # chromatic
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.375), # D2
]
bass.notes.extend(bass_notes)

# Diane - Piano: Open voicings, resolve on the last beat of each bar
piano_notes = [
    # Bar 2: Dmaj7 (D F# A C#) - open voicing
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875), # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875), # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875), # A4
    pretty_midi.Note(velocity=80, pitch=76, start=1.5, end=1.875), # C#5

    # Bar 3: G7 (G B D F) - open voicing
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.75), # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.375, end=2.75), # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.375, end=2.75), # D5
    pretty_midi.Note(velocity=80, pitch=76, start=2.375, end=2.75), # F5

    # Bar 4: Amin7 (A C E G) - open voicing
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75), # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75), # C5
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75), # E5
    pretty_midi.Note(velocity=80, pitch=79, start=3.375, end=3.75), # G5
]
piano.notes.extend(piano_notes)

# Little Ray - Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth (Bar 2-4)
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

# Dante - Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (E4), F4, G4 (G4), F4, E4 (D4)
# Start at 1.5 (Bar 2), play first three notes
note1 = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75) # D4
note2 = pretty_midi.Note(velocity=105, pitch=64, start=1.75, end=2.0) # E4
note3 = pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25) # F4
note4 = pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5) # G4
note5 = pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75) # F4
note6 = pretty_midi.Note(velocity=105, pitch=64, start=2.75, end=3.0) # E4
note7 = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25) # D4

sax.notes.extend([note1, note2, note3, note4, note5, note6, note7])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
