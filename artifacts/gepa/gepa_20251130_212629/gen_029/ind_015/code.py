
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor sax is program 64
pm.instruments.append(instrument)

# Set tempo (160 BPM)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0, crochet=0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(tempo=160.0, time=0.0)]

# Time per beat in seconds
beat_time = 60.0 / 160.0

# Function to convert bar/beat to time
def bar_beat_to_time(bar, beat):
    return bar * 4 * beat_time + beat * beat_time

# Bar 1: Little Ray (drums) only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 0.0 to 1.5 seconds

# Kick on 1 (bar 1, beat 1)
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_beat_to_time(0, 1), end=bar_beat_to_time(0, 1) + 0.1)
instrument.notes.append(kick_1)

# Kick on 3 (bar 1, beat 3)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_beat_to_time(0, 3), end=bar_beat_to_time(0, 3) + 0.1)
instrument.notes.append(kick_3)

# Snare on 2 (bar 1, beat 2)
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_beat_to_time(0, 2), end=bar_beat_to_time(0, 2) + 0.1)
instrument.notes.append(snare_2)

# Snare on 4 (bar 1, beat 4)
snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_beat_to_time(0, 4), end=bar_beat_to_time(0, 4) + 0.1)
instrument.notes.append(snare_4)

# Hi-hat on every eighth note
for i in range(1, 9):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=bar_beat_to_time(0, i/2), end=bar_beat_to_time(0, i/2) + 0.05)
    instrument.notes.append(hihat)

# Bar 2-4: The rest of the band comes in, tenor takes the melody

# Diane (piano) — 7th chords, comp on 2 and 4
# Dm7: D, F, A, C
diane_notes = [
    # Bar 2, beat 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=bar_beat_to_time(1, 2), end=bar_beat_to_time(1, 2) + 0.2),
    pretty_midi.Note(velocity=90, pitch=65, start=bar_beat_to_time(1, 2), end=bar_beat_to_time(1, 2) + 0.2),
    pretty_midi.Note(velocity=90, pitch=67, start=bar_beat_to_time(1, 2), end=bar_beat_to_time(1, 2) + 0.2),
    pretty_midi.Note(velocity=90, pitch=69, start=bar_beat_to_time(1, 2), end=bar_beat_to_time(1, 2) + 0.2),
    
    # Bar 3, beat 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=bar_beat_to_time(2, 2), end=bar_beat_to_time(2, 2) + 0.2),
    pretty_midi.Note(velocity=90, pitch=65, start=bar_beat_to_time(2, 2), end=bar_beat_to_time(2, 2) + 0.2),
    pretty_midi.Note(velocity=90, pitch=67, start=bar_beat_to_time(2, 2), end=bar_beat_to_time(2, 2) + 0.2),
    pretty_midi.Note(velocity=90, pitch=69, start=bar_beat_to_time(2, 2), end=bar_beat_to_time(2, 2) + 0.2),
    
    # Bar 4, beat 4: Dm7 (shorter to leave it hanging)
    pretty_midi.Note(velocity=90, pitch=62, start=bar_beat_to_time(3, 4), end=bar_beat_to_time(3, 4) + 0.15),
    pretty_midi.Note(velocity=90, pitch=65, start=bar_beat_to_time(3, 4), end=bar_beat_to_time(3, 4) + 0.15),
    pretty_midi.Note(velocity=90, pitch=67, start=bar_beat_to_time(3, 4), end=bar_beat_to_time(3, 4) + 0.15),
    pretty_midi.Note(velocity=90, pitch=69, start=bar_beat_to_time(3, 4), end=bar_beat_to_time(3, 4) + 0.15),
]

for note in diane_notes:
    instrument.notes.append(note)

# Marcus (bass) - walking line in Dm, chromatic approaches, no repeating notes
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Walking line: D, F, Eb, G, A, Bb, C, D (chromatic approach to F)
# Let’s map this over 4 bars, 4 beats per bar, with chromatic passes

bass_notes = [
    # Bar 2, beat 1: D
    pretty_midi.Note(velocity=80, pitch=62, start=bar_beat_to_time(1, 1), end=bar_beat_to_time(1, 1) + 0.25),
    
    # Bar 2, beat 2: F
    pretty_midi.Note(velocity=80, pitch=67, start=bar_beat_to_time(1, 2), end=bar_beat_to_time(1, 2) + 0.25),
    
    # Bar 2, beat 3: Eb
    pretty_midi.Note(velocity=80, pitch=64, start=bar_beat_to_time(1, 3), end=bar_beat_to_time(1, 3) + 0.25),
    
    # Bar 2, beat 4: G
    pretty_midi.Note(velocity=80, pitch=69, start=bar_beat_to_time(1, 4), end=bar_beat_to_time(1, 4) + 0.25),
    
    # Bar 3, beat 1: A
    pretty_midi.Note(velocity=80, pitch=71, start=bar_beat_to_time(2, 1), end=bar_beat_to_time(2, 1) + 0.25),
    
    # Bar 3, beat 2: Bb
    pretty_midi.Note(velocity=80, pitch=70, start=bar_beat_to_time(2, 2), end=bar_beat_to_time(2, 2) + 0.25),
    
    # Bar 3, beat 3: C
    pretty_midi.Note(velocity=80, pitch=67, start=bar_beat_to_time(2, 3), end=bar_beat_to_time(2, 3) + 0.25),
    
    # Bar 3, beat 4: D
    pretty_midi.Note(velocity=80, pitch=62, start=bar_beat_to_time(2, 4), end=bar_beat_to_time(2, 4) + 0.25),
    
    # Bar 4, beat 1: F
    pretty_midi.Note(velocity=80, pitch=67, start=bar_beat_to_time(3, 1), end=bar_beat_to_time(3, 1) + 0.25),
    
    # Bar 4, beat 2: Eb
    pretty_midi.Note(velocity=80, pitch=64, start=bar_beat_to_time(3, 2), end=bar_beat_to_time(3, 2) + 0.25),
    
    # Bar 4, beat 3: G
    pretty_midi.Note(velocity=80, pitch=69, start=bar_beat_to_time(3, 3), end=bar_beat_to_time(3, 3) + 0.25),
    
    # Bar 4, beat 4: A (leave it hanging)
    pretty_midi.Note(velocity=80, pitch=71, start=bar_beat_to_time(3, 4), end=bar_beat_to_time(3, 4) + 0.15),
]

for note in bass_notes:
    instrument.notes.append(note)

# Tenor sax (you) — one short motif, starts it, leaves it hanging
# Dm mode: D, Eb, F, G, A, Bb, C
# Melody: D -> Eb (half step), F -> G (whole step), A -> Bb (half step), C (half step)
# Let’s phrase it over 3 beats, with a rest on the 4th

tenor_notes = [
    # Bar 2, beat 1: D
    pretty_midi.Note(velocity=110, pitch=62, start=bar_beat_to_time(1, 1), end=bar_beat_to_time(1, 1) + 0.3),
    
    # Bar 2, beat 2: Eb
    pretty_midi.Note(velocity=110, pitch=64, start=bar_beat_to_time(1, 2), end=bar_beat_to_time(1, 2) + 0.3),
    
    # Bar 2, beat 3: F
    pretty_midi.Note(velocity=110, pitch=67, start=bar_beat_to_time(1, 3), end=bar_beat_to_time(1, 3) + 0.3),
    
    # Bar 2, beat 4: G
    pretty_midi.Note(velocity=110, pitch=69, start=bar_beat_to_time(1, 4), end=bar_beat_to_time(1, 4) + 0.3),
    
    # Bar 3, beat 1: A
    pretty_midi.Note(velocity=110, pitch=71, start=bar_beat_to_time(2, 1), end=bar_beat_to_time(2, 1) + 0.3),
    
    # Bar 3, beat 2: Bb
    pretty_midi.Note(velocity=110, pitch=70, start=bar_beat_to_time(2, 2), end=bar_beat_to_time(2, 2) + 0.3),
    
    # Bar 3, beat 3: C
    pretty_midi.Note(velocity=110, pitch=67, start=bar_beat_to_time(2, 3), end=bar_beat_to_time(2, 3) + 0.3),
    
    # Bar 4, beat 1: D
    pretty_midi.Note(velocity=110, pitch=62, start=bar_beat_to_time(3, 1), end=bar_beat_to_time(3, 1) + 0.3),
    
    # Bar 4, beat 2: Eb
    pretty_midi.Note(velocity=110, pitch=64, start=bar_beat_to_time(3, 2), end=bar_beat_to_time(3, 2) + 0.3),
    
    # Bar 4, beat 3: F
    pretty_midi.Note(velocity=110, pitch=67, start=bar_beat_to_time(3, 3), end=bar_beat_to_time(3, 3) + 0.3),
    
    # Bar 4, beat 4: Hold on, leave it unplayed
]

for note in tenor_notes:
    instrument.notes.append(note)

# Write the MIDI file
pm.write('dante_introduction.mid')
