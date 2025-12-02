
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

# Kick on 1 and 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)
drums.notes.extend([drum_kick_1, drum_kick_3])

# Snare on 2 and 4
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)
drums.notes.extend([drum_snare_2, drum_snare_4])

# Hi-hat on every eighth
for i in range(8):
    start = i * 0.375
    end = start + 0.375
    hi_hat = pretty_midi.Note(velocity=80, pitch=42, start=start, end=end)
    drums.notes.append(hi_hat)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
# Dm7: D F A C
# Walking bass line in Dm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on 2 and 4 (beat 2 and 4 of each bar)

# Bar 2: 2nd beat (0.75-1.125) and 4th beat (1.875-2.25)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25), # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25), # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25), # C
]

# Bar 3: 2nd beat (2.625-3.0) and 4th beat (3.75-4.125)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125), # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125), # C
])

# Bar 4: 2nd beat (4.5-4.875) and 4th beat (5.625-6.0)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0), # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0), # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0), # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0), # C
])

piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)
drums.notes.extend([drum_kick_1, drum_kick_3, drum_snare_2, drum_snare_4])

# Bar 3
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)
drums.notes.extend([drum_kick_1, drum_kick_3, drum_snare_2, drum_snare_4])

# Bar 4
drum_kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drum_snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drums.notes.extend([drum_kick_1, drum_kick_3, drum_snare_2, drum_snare_4])

# Dante: Tenor sax melody
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif (D to F to A)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
]

# Bar 3: Leave it hanging (rest)
# Bar 4: Come back and finish it (A to C to D to F)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # F
])

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
