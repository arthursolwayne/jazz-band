
import pretty_midi

# Initialize MIDI file with 160 BPM
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

# Time in seconds for each bar (4/4 at 160 BPM)
BAR_DURATION = 1.5
BEAT_DURATION = BAR_DURATION / 4

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    start = bar * BAR_DURATION
    # Kick on beat 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Snare on beat 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth note
    for eighth in range(8):
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=start + eighth * BEAT_DURATION / 2, 
                                end=start + eighth * BEAT_DURATION / 2 + 0.05)
        drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.5 + 0.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.75, end=2.0),        # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.25),        # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5),        # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),        # E
    pretty_midi.Note(velocity=80, pitch=62, start=2.75, end=3.0),        # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),        # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),        # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.5, end=3.75),        # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.0),        # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.0, end=4.25),        # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.25, end=4.5),        # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),        # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),        # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.0, end=5.25),        # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.5),        # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.75),        # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=6.0),        # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Dm7 = D F A C
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.75, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.75, end=3.0),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.5),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.75, end=6.0),   # A
]
sax.notes.extend(sax_notes)

# Drums: Continue with kick on 1 and 3, snare on 2 and 4, hihat every eighth
for bar in range(2, 4):  # bars 2 and 3 (1.5 to 6.0s)
    start = bar * BAR_DURATION
    # Kick on beat 1 and 3
    for beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Snare on beat 2 and 4
    for beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=drum_notes['snare'], start=start + beat * BEAT_DURATION, end=start + beat * BEAT_DURATION + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth note
    for eighth in range(8):
        note = pretty_midi.Note(velocity=80, pitch=drum_notes['hihat'], start=start + eighth * BEAT_DURATION / 2, 
                                end=start + eighth * BEAT_DURATION / 2 + 0.05)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
