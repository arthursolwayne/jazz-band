
import pretty_midi

# Initialize MIDI file with tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time in seconds per bar at 160 BPM
bar_length = 1.5  # 60 / 160 * 4 = 1.5 seconds per bar

# BAR 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 - 1.5s
for i in range(4):
    time = i * 0.375  # 1/8 note
    if i % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=90, pitch=drum_notes['kick'], start=time, end=time + 0.125)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=90, pitch=drum_notes['snare'], start=time, end=time + 0.125)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=60, pitch=drum_notes['hihat'], start=time, end=time + 0.125)
    drums.notes.append(note)

# BAR 2 - 4: Full quartet (1.5 - 6.0s)

# BASS LINE: Walking line in F minor with chromatic approaches
# F minor: F, Gb, Ab, Bb, B, Db, Eb
bass_notes = [
    # Bar 2: F - Gb - Ab - Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.5 + 0.25),  # F3
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=1.75 + 0.25),  # Gb3
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.0 + 0.25),  # Ab3
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.25 + 0.25),  # Bb3

    # Bar 3: B - Db - Eb - F
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.5 + 0.25),  # B3
    pretty_midi.Note(velocity=80, pitch=66, start=2.75, end=2.75 + 0.25),  # Db3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.0 + 0.25),  # Eb3
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.25 + 0.25),  # F3

    # Bar 4: Gb - Ab - Bb - B
    pretty_midi.Note(velocity=80, pitch=70, start=3.5, end=3.5 + 0.25),  # Gb3
    pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=3.75 + 0.25),  # Ab3
    pretty_midi.Note(velocity=80, pitch=67, start=4.0, end=4.0 + 0.25),  # Bb3
    pretty_midi.Note(velocity=80, pitch=69, start=4.25, end=4.25 + 0.25),  # B3
]

bass.notes.extend(bass_notes)

# PIANO: 7th chords, comp on 2 and 4, F minor
# F7 = F, A, C, Eb

# Bar 2: comp on beat 2
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.75, end=1.75 + 0.125),  # F3
    pretty_midi.Note(velocity=80, pitch=74, start=1.75, end=1.75 + 0.125),  # A3
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=1.75 + 0.125),  # C4
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=1.75 + 0.125),  # Eb4

    # Bar 3: comp on beat 2
    pretty_midi.Note(velocity=80, pitch=71, start=2.75, end=2.75 + 0.125),  # F3
    pretty_midi.Note(velocity=80, pitch=74, start=2.75, end=2.75 + 0.125),  # A3
    pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=2.75 + 0.125),  # C4
    pretty_midi.Note(velocity=80, pitch=70, start=2.75, end=2.75 + 0.125),  # Eb4

    # Bar 4: comp on beat 2
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=3.75 + 0.125),  # F3
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=3.75 + 0.125),  # A3
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=3.75 + 0.125),  # C4
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=3.75 + 0.125),  # Eb4
]

piano.notes.extend(piano_notes)

# SAX: Your moment. One short motif. Start, leave it hanging, come back and finish it.
# In F minor, sax begins with a short motif: F - Bb - Gb - F (with a slight delay on the Gb to make it sing)

sax_notes = [
    pretty_midi.Note(velocity=96, pitch=71, start=1.5, end=1.5 + 0.25),  # F3
    pretty_midi.Note(velocity=96, pitch=67, start=1.75, end=1.75 + 0.125),  # Bb3 (half note)
    pretty_midi.Note(velocity=96, pitch=70, start=2.0, end=2.0 + 0.25),  # Gb3
    pretty_midi.Note(velocity=96, pitch=71, start=2.5, end=2.5 + 0.25),  # F3
]

sax.notes.extend(sax_notes)

# BAR 1: Drums only
# BAR 2-4: Full quartet

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to MIDI file
midi.write("dante_intro.mid")
