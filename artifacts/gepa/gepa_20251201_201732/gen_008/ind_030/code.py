
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS LINE - Marcus
# Fm7 -> Bb7 -> Eb7 -> Am7
# Roots: F, Bb, Eb, A (Fm key)
# Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.625, end=1.75), # Gb
    pretty_midi.Note(velocity=90, pitch=37, start=1.75, end=1.875), # E
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0), # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.125), # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=2.125, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375), # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=2.375, end=2.5), # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=47, start=2.5, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=2.75), # F
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=2.875), # E
    pretty_midi.Note(velocity=90, pitch=47, start=2.875, end=3.0), # Eb
    # Bar 5
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.125), # A
    pretty_midi.Note(velocity=90, pitch=52, start=3.125, end=3.25), # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.375), # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.5), # A
]
bass.notes.extend(bass_notes)

# PIANO - Diane
# Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625), # C (Fm7)
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625), # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625), # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=58, start=2.0, end=2.125), # Bb (Bb7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125), # Ab
])
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.625), # Eb (Eb7)
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625), # D
])
# Bar 5: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.125), # A (Am7)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.125), # C
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.125), # E
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.125), # G
])
piano.notes.extend(piano_notes)

# SAX - Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 -> Bb7 -> Eb7 -> Am7
# Motif: F - Ab - D - Bb (Fm7) then a leap to E and back to F
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625), # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.625, end=1.75), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0), # D
    # Bar 3: Continue
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125), # E
    pretty_midi.Note(velocity=110, pitch=53, start=2.125, end=2.25), # F
    pretty_midi.Note(velocity=110, pitch=57, start=2.25, end=2.375), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5), # D
    # Bar 4: Introduce tension
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.625), # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75), # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.75, end=2.875), # D
    pretty_midi.Note(velocity=110, pitch=53, start=2.875, end=3.0), # F
    # Bar 5: Resolve
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.125), # F
    pretty_midi.Note(velocity=110, pitch=57, start=3.125, end=3.25), # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.375), # D
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.5), # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4 continue with same pattern
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.75) # Hi-hat
]
for i in range(6):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5 + i*0.125, end=1.5 + (i+1)*0.125))
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.25) # Hi-hat
]
for i in range(6):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.0 + i*0.125, end=2.0 + (i+1)*0.125))
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.875), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75) # Hi-hat
]
for i in range(6):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.5 + i*0.125, end=2.5 + (i+1)*0.125))
drums.notes.extend(drum_notes)

# Bar 5
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.25) # Hi-hat
]
for i in range(6):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0 + i*0.125, end=3.0 + (i+1)*0.125))
drums.notes.extend(drum_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
midi.write("dante_intro.mid")
