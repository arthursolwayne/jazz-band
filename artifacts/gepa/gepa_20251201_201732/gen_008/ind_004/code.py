
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Fm, roots and fifths with chromatic approaches
# Fm: F, Ab, C, D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.875),  # Ab (root)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25), # D (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # Bb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=37, start=2.625, end=3.0),  # Ab (root)
    pretty_midi.Note(velocity=90, pitch=41, start=3.0, end=3.375),  # D (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # Eb (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # D (fifth)
    pretty_midi.Note(velocity=90, pitch=37, start=4.125, end=4.5),  # Ab (root)
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # D (fifth)
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25), # B (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=41, start=5.25, end=5.625), # D (fifth)
    pretty_midi.Note(velocity=90, pitch=37, start=5.625, end=6.0),  # Ab (root)
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.5, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=56, start=1.5, end=2.25), # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=3.0), # Bb
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=3.0), # Ab
]
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.75), # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=3.75), # Bb
]
# Resolutions on the last beat of each bar
piano_notes_bar2.append(pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.625))
piano_notes_bar3.append(pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375))
piano_notes_bar4.append(pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125))
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - G - Ab - C (motif 1), then F - Ab - C (motif 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875), # F
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=53, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(start_time):
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 0.0, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.5, end=start_time + 1.875)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 2.25, end=start_time + 2.625)
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.0, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.375, end=start_time + 0.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 0.75, end=start_time + 1.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.125, end=start_time + 1.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.5, end=start_time + 1.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 1.875, end=start_time + 2.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.25, end=start_time + 2.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 2.625, end=start_time + 3.0)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.0, end=start_time + 3.375)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.375, end=start_time + 3.75)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 3.75, end=start_time + 4.125)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 4.125, end=start_time + 4.5)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 4.5, end=start_time + 4.875)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 4.875, end=start_time + 5.25)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 5.25, end=start_time + 5.625)
    pretty_midi.Note(velocity=100, pitch=42, start=start_time + 5.625, end=start_time + 6.0)

add_drums(1.5)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
